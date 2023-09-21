# assignment 1
# def get_score(**subjects):
#     for key, value in subjects.items():
#         print(f"{key} => {value}")
# get_score(Math=90, Science=80, Language=70)
# assignment 2
# def get_people_scores(name="", **subjects):
#     if subjects:
#         if name:
#             print(f"Hello {name} this is your score: ")
#         for key, value in subjects.items():
#             print(f"{key} => {value}")
#     else:
#         print(f"Hello {name} You Have No Scores To Show.")
# get_people_scores(Logic=70, Problems=60)
# assignment 3
# scores_list={
#     "Math":"90",
#     "science":"80",
#     "language":"70"
# }
# def get_the_scores(name="", **subjects):
#     if subjects:
#         if name:
#             print(f"Hello {name} this is your score: ")
#         for key, value in subjects.items():
#             print(f"{key} => {value}")
#     else:
#         print(f"Hello {name} You Have No Scores To Show.")
# get_the_scores(**scores_list)