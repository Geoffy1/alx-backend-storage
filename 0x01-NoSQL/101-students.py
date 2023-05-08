def top_students(mongo_collection):
    pipeline = [
        {
            '$project': {
                'name': 1,
                'scores': 1,
                'averageScore': {'$avg': '$scores.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))

