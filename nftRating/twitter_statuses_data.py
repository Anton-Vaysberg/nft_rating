import bigQuery
from bigQuery import *
from twython import Twython
from sentiment import *

t = Twython(app_key='CV0IDw8fZ9k0jRKmzfEbKoESS',
            app_secret='yDjfZ39VLTjWrOVmrbZcu0N5L85vzOZPg6fuyJbMnctfKF997V',
            )

statuses_full_list = []
twitter_statuses_data_list = []
users_lst = get_twitter_users_id()
users_count = get_rows_count(raw_data_table_id)
i = 0
for row in users_lst:
    i += 1
    twitter_statuses_data = {}
    print("{}".format(row.twitter_user_id))

    try:
        statuses_data = t.get_user_timeline(id=row.twitter_user_id)
    except Exception as ex:
        print(ex)
        continue

    for status_payload in statuses_data:
        status_full = {}
        status = status_payload['text']
        try:
            status_sentiment = analyze_sentiment(status_payload['text'])
        except Exception as ex:
            print(ex)
            status_sentiment = 0
        status_full.update({"uuid": row.uuid, "twitter_user_id": row.twitter_user_id, "twitter_status": status,
                            "status_sentiment": status_sentiment})
        statuses_full_list.append(status_full)
    print("{} user processed from {}.".format(i, users_count))

insert_rows_from_json(twitter_statuses_table_id, statuses_full_list)

