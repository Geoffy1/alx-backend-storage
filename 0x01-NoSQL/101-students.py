#!/usr/bin/env python3
"""function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Prints all students in a collection sorted by average score.
    """
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {'$avg': '$topics.score'},
                'topics': 1,
            },
        },
        {
            '$sort': {'averageScore': -1},
        },
    ]
    students = mongo_collection.aggregate(pipeline)
    return students
