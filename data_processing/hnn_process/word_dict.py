import pickle


# 构建初步词典的具体步骤1
def get_vocab(corpus1, corpus2):
    word_vacab = set()
    for corpus in [corpus1, corpus2]:
        for i in range(len(corpus)):
            for j in range(len(corpus[i][1][0])):
                word_vacab.add(corpus[i][1][0][j])
            for j in range(len(corpus[i][1][1])):
                word_vacab.add(corpus[i][1][1][j])
            for j in range(len(corpus[i][2][0])):
                word_vacab.add(corpus[i][2][0][j])
            for j in range(len(corpus[i][3])):
                word_vacab.add(corpus[i][3][j])
    print(len(word_vacab))
    return word_vacab


def load_pickle(filename):
    return pickle.load(open(filename, 'rb'), encoding='iso-8859-1')


# 构建初步词典
def vocab_prpcessing(filepath1, filepath2, save_path):
    with open(filepath1, 'r') as f:
        eval(f.read())
        f.close()

    with open(filepath2, 'r') as f:
        total_data2 = eval(f.read())
        f.close()

    x1 = get_vocab(total_data2, total_data2)
    # total_data_sort = sorted(x1, key=lambda x: (x[0], x[1]))
    f = open(save_path, "w")
    f.write(str(x1))
    f.close()


def final_vocab_prpcessing(filepath1, filepath2, save_path):
    word_set = set()
    with open(filepath1, 'r') as f:
        total_data1 = set(eval(f.read()))
        f.close()
    with open(filepath2, 'r') as f:
        total_data2 = eval(f.read())
        f.close()
    total_data1 = list(total_data1)
    x1 = get_vocab(total_data2, total_data2)
    # total_data_sort = sorted(x1, key=lambda x: (x[0], x[1]))
    for i in x1:
        if i in total_data1:
            continue
        else:
            word_set.add(i)
    print(len(total_data1))
    print(len(word_set))
    f = open(save_path, "w")
    f.write(str(word_set))
    f.close()


if __name__ == "__main__":
    # 写你妈绝对路径呢？
    # ====================获取staqc的词语集合===============
    python_hnn = './data/python_hnn_data_teacher.txt'
    python_staqc = './data/staqc/python_staqc_data.txt'
    python_word_dict = './data/word_dict/python_word_vocab_dict.txt'

    sql_hnn = './data/sql_hnn_data_teacher.txt'
    sql_staqc = './data/staqc/sql_staqc_data.txt'
    sql_word_dict = './data/word_dict/sql_word_vocab_dict.txt'

    # vocab_prpcessing(python_hnn,python_staqc,python_word_dict)
    # vocab_prpcessing(sql_hnn,sql_staqc,sql_word_dict)
    # ====================获取最后大语料的词语集合的词语集合===============
    new_sql_staqc = './ulabel_data/staqc/sql_staqc_unlabled_data.txt'
    new_sql_large = './ulabel_data/large_corpus/multiple/sql_large_multiple_unlable.txt'
    large_word_dict_sql = './ulabel_data/sql_word_dict.txt'
    final_vocab_prpcessing(sql_word_dict, new_sql_large, large_word_dict_sql)
    # vocab_prpcessing(new_sql_staqc,new_sql_large,final_word_dict_sql)

    new_python_staqc = '../ulabel_data/staqc/python_staqc_unlabled_data.txt'
    new_python_large = './ulabel_data/large_corpus/multiple/python_large_multiple_unlable.txt'
    large_word_dict_python = './ulabel_data/python_word_dict.txt'
    # final_vocab_prpcessing(python_word_dict, new_python_large, large_word_dict_python)
    # vocab_prpcessing(new_python_staqc,new_python_large,final_word_dict_python)