#Exercise 4
def has_experience_as(list_cv,job_title):
    result=[]
    for x in list_cv:
        if job_title in x['jobs']:
            result.append(x['user'])
    return result

cv= [{'user': 'john', 'jobs': ['analyst', 'engineer']},
      {'user': 'jane', 'jobs': ['finance', 'software']},
      {'user':'jessica', 'jobs':['finance','analyst']}]
finance_people=has_experience_as(cv, 'finance')
print(finance_people)


# 5)
def job_counts(cv_data: list[dict]) -> dict:
    result = {}
    for cv in cv_data:
        for job in cv["jobs"]:
            if job in result:
                result[job] += 1
            else:
                result[job] = 1
    
    return result

print(job_counts(cv_data=[{'user': 'john', 'jobs': ['analyst', 'engineer']}, 
                          {'user': 'jane', 'jobs': ['finance', 'software']},
                          {'user': '1', 'jobs': ["cowbreeder"]},
                          {'user': '2', 'jobs': ['finance',]},
                          {'user': '3', 'jobs': ['software']}]))


# 6)
def most_popular_job(cv_data: list[dict]):
    counts = job_counts(cv_data=cv_data)

    return max(counts.items(), key=lambda i: i[1])

print(most_popular_job(cv_data=[{'user': 'john', 'jobs': ['analyst', 'engineer']}, 
                          {'user': 'jane', 'jobs': ['finance', 'software']},
                          {'user': '1', 'jobs': ["cowbreeder"]},
                          {'user': '2', 'jobs': ['finance',]},
                          {'user': '3', 'jobs': ['finance']}]))