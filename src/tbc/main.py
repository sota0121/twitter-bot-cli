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
    import random
    from datetime import date
    from wrapper import TweepyWrapper as tw
    from wrapper import GspreadWrapper as gw
    from wrapper import GCSWrapper as gcsw

    # gs_api = gw()
    # tweets_list = gs_api.tweets
    gcs_app = gcsw()
    tweets_df = gcs_app.tweets_df
    #tweets_list = gcs_app.tweets

    today_date = date.today().day
    df_target_idx = today_date - 1
    df_target_row = tweets_df.iloc[df_target_idx]

    tweet_str = df_target_row['text']
    img_name = str(df_target_row['imgName'])
    out_img_path = f"./{img_name}"
    img_file = gcs_app.download_image_by_name(img_name)

    # # == init tweet list ==
    # tweets = []
    # flgs_tweeted = []
    # for t in tweets_list:
    #     tweets.append(t['text'])
    #     flgs_tweeted.append(t['tweeted'])
    # tweeted_all = [1] * len(flgs_tweeted)
    # if flgs_tweeted == tweeted_all:
    #     flgs_tweeted = [0] * len(flgs_tweeted)

    # # == extract not tweeted ==
    # tgt_idxes = [idx for idx, elm in enumerate(flgs_tweeted) if (elm == 0)]
    # print("target idx : ", " ".join(map(str, tgt_idxes)))
    # selected_idx = random.choice(tgt_idxes)
    # # - update
    # flgs_tweeted[selected_idx] = 1
    # tweets_list_ = [{'text': t, 'tweeted': f} for t, f in zip(tweets, flgs_tweeted)]
    # gcs_app.update_tweets(tweets_list_)

    # sended words
    tw_app = tw()
    media = tw_app.api.media_upload(filename="img.jpg", file=img_file)
    result = tw_app.api.update_status(status=tweet_str, media_ids=[media.media_id])
    return f'tweeted > \n{tweet_str}'

    # parsing requests if needed
    # request_json = request.get_json()
    # if request.args and 'message' in request.args:
    #     return request.args.get('message')
    # elif request_json and 'message' in request_json:
    #     return request_json['message']
    # else:
    #     return f'message does not exists as key.'
