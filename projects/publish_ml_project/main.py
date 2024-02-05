# when publishing on the web app --> model have to be pre-trained
# make model reusable to avoid it being trained on EACH run ! --> use joblib library --> pip3 install joblib

from projects.publish_ml_project.model.model import predict_salary

# salary = predict_salary(8, 3)
# salary = predict_salary(level=3, experience=8)
salary = "9999"  # predict_salary(experience=8, level=3)

print(salary)

# 3391.8922119768276
