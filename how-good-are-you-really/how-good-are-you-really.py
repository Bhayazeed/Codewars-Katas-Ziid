def better_than_average(class_points, your_points):
    #mencari rata-rata nilai kelas lalu bandingkan dengan nilai ktia
    all_points = sum(class_points)
    average = all_points // len(class_points)
    return average < your_points