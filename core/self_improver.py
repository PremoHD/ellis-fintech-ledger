from memory.long_term import store_experience

def improve(task, result, score):
    store_experience({
        "task": task,
        "result": result,
        "score": score
    })