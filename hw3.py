def quick_sort(arr):                                             #定義了一個名為 quick_sort 的函式，用於進行快速排序。
    if len(arr) <= 1:                                            #當輸入的陣列長度小於等於1時，直接返回該陣列。
        return arr
    else:                                                        #當輸入的陣列長度不是小於等於1時，表示仍然需要進行排序。
        pivot = arr[0]                                           #將陣列的第一個元素作為基準點。
        smaller_than_pivot = [x for x in arr[1:] if x <= pivot]  #創建一個新的陣列，其中包含所有小於等於基準點的元素。
        bigger_than_pivot = [x for x in arr[1:] if x > pivot]    #創建一個新的陣列，其中包含所有大於基準點的元素。
        sorted_small = quick_sort(smaller_than_pivot)            #遞迴地對小於基準點的陣列進行快速排序。
        sorted_big = quick_sort(bigger_than_pivot)               #遞迴地對大於基準點的陣列進行快速排序。
        sorted_arr = sorted_small + [pivot] + sorted_big         #將排好序的小於基準點的陣列、基準點、排好序的大於基準點的陣列組合成一個新的排好序的陣列。
        print(sorted_arr)                                        #印出排序過程。
        return sorted_arr                                        #返回排好序的陣列。


# Demo
arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]                    #這次上課講義中範例的陣列 arr。
print("Original array:", arr)                                    #印出原始的未排序陣列，這樣我們就可以在排序之前看到它的狀態。
sorted_arr = quick_sort(arr)                                     #調用剛剛定義的 quick_sort 函式，並將示例陣列 arr 作為參數傳遞給它，這將對陣列進行排序。
print("Sorted array:", sorted_arr)                               #印出排序後的陣列，這樣我們就可以在排序之後看到它的狀態。
