def send_tweet(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Importing the libraries we'll use
    import gspread
    import json
    import random
    import tweepy
    from google.cloud import storage
    from os import getenv

    # == Twitter authorisation ==
    # Getting the key and secret codes from my environment variables
    consumer_key = getenv("consumer_key")
    consumer_secret = getenv("consumer_secret")
    access_token = getenv("access_token")
    access_secret = getenv("access_secret")

    # Tweepy's process for setting up authorisation
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # == Google Spread Sheet authorisation ==
    # Getting the key and secret codes from my environment variables
    credentials = {
        "TYPE": getenv("gs_type"),
        "PROJECT_ID": getenv("gs_project_id"),
        "PRIVATE_KEY_ID": getenv("gs_private_key_id"),
        "PRIVATE_KEY": getenv("gs_private_key"),
        "CLIENT_EMAIL": getenv("gs_client_email"),
        "CLIENT_ID": getenv("gs_client_id"),
        "AUTH_URI": getenv("gs_auth_uri"),
        "TOKEN_URI": getenv("gs_token_uri"),
        "AUTH_PROVIDER_X509_CERT_URL": getenv("gs_auth_provider_x509_cert_url"),
        "CLIENT_X509_CERT_URL": getenv("gs_client_x509_cert_url")
    }

    print(credentials)

    # gc = gspread.service_account_from_dict(credentials)
    # sh = gc.open("twitter-bot-positive-demon")
    # print(sh.sheet1.get('A1'))
    # tweet_list = sh.sheet1.col_values(1)[1:]

    # == Google Cloud Storage auth ==
    storage_client = storage.Client()
    bucket_name = "tweet-source"
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob("tweets_list.json")
    blob_txt = blob.download_as_text()
    tweets_list = json.loads(blob_txt)

    # == init tweet list ==
    tweets = []
    flgs_tweeted = []
    for t in tweets_list:
        tweets.append(t['text'])
        flgs_tweeted.append(t['tweeted'])
    tweeted_all = [1] * len(flgs_tweeted)
    if flgs_tweeted == tweeted_all:
        flgs_tweeted = [0] * len(flgs_tweeted)

    # == extract not tweeted ==
    tgt_idxes = [idx for idx, elm in enumerate(flgs_tweeted) if (elm == 0)]
    print("target idx : ", " ".join(map(str, tgt_idxes)))
    selected_idx = random.choice(tgt_idxes)
    # - update
    flgs_tweeted[selected_idx] = 1
    tweets_list_ = [{'text': t, 'tweeted': f} for t, f in zip(tweets, flgs_tweeted)]
    try:
        blob.upload_from_string(data=json.dumps(tweets_list_), content_type='application/json')
    except:
        print('failed to upload json (I will solve this problem in a few days.)')

    # sended words
    tweet = tweets[selected_idx]
    api.update_status(tweet)
    return f'tweeted > \n{tweet}'

    # parsing requests if needed
    # request_json = request.get_json()
    # if request.args and 'message' in request.args:
    #     return request.args.get('message')
    # elif request_json and 'message' in request_json:
    #     return request_json['message']
    # else:
    #     return f'message does not exists as key.'
