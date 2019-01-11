def mice_fill(dataframe):
    if dataframe.isnull().sum().sum() > 0:

        # 통째로 빈 컬럼 찾아낸 후 버리기
        entireNull = dataframe.columns[dataframe.isnull().sum().values == len(dataframe)]
        dataframe_ = dataframe.drop(entireNull, axis=1)

        # array 형식에 맞지않은 컬럼 제거
        unacceptable_var = [x for x in dataframe.columns if str(dataframe[x].dtypes) not in ['float64', 'int64']]
        backup_data = dataframe[unacceptable_var]
        backup_data_index = []

        same_name_check = []
        for i in unacceptable_var:

            if i in same_name_check:
                ind = list(dataframe_.columns[list(dataframe_.columns).index(i) + 1:]).index(i)
                backup_data_index.append(ind)

            else:

                ind = list(dataframe_.columns).index(i)
                backup_data_index.append(ind)
            same_name_check.append(i)

        dataframe__ = dataframe_.drop(unacceptable_var, axis=1)
        columns = dataframe__.columns
        dataframe__ = dataframe__.astype(np.float64)

        # mice 시도
        arr = np.array(dataframe__.values)
        miced = MICE(n_imputations=20, impute_type='col', n_burn_in=10).complete(arr)
        dataframe_miced = pd.DataFrame(miced, columns=columns)
        #         print('backup_index', backup_data_index, 'unaccept:', unacceptable_var)

        # 분리했던 열 다시 추가하기
        for loc, col in zip(backup_data_index, unacceptable_var):
            #             print('loc :',loc , 'col:', col)
            dataframe_miced.insert(loc=loc, column=col, value=dataframe[[col]].iloc[:, [0]], allow_duplicates=True)
        print('imputation succeed :)')
        return dataframe_miced

    else:
        return dataframe