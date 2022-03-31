import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import cv2



"""
1. A company needs to analyze the new covid stats for march 28th 2022.
Download csv file os those stats and plot them on a bar graph
"""

def download_and_plot_data():
    live_covid_data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    df = pd.read_csv(live_covid_data_url)
    df.head()
    df.tail()
    df.dropna(inplace=True)
    df.drop(['Lat','Long'],axis=1,inplace=True)
    # plot data for only 27th march 2022
    df_27th_march_2022 = df.loc[df['3/27/22']>0]
    # create a new df with only 'Country/Region' and '3/27/22' columns
    df_27th_march_2022 = df_27th_march_2022[['Country/Region','3/27/22']]
    # save to a csv file
    df_27th_march_2022.to_csv('27th_march_2022.csv')
    # plot data
    df_27th_march_2022.head()
    df_27th_march_2022.tail()
    df_27th_march_2022.plot(kind='bar', x=df_27th_march_2022['Country/Region'] , y=df_27th_march_2022['3/27/22'])
    plt.show()


# download_and_plot_data()

"""
2. Those same stats, the company wants you to find the total average of new cases from each country.
"""

def total_average_of_new_cases_from_each_country():
    df = pd.read_csv('27th_march_2022.csv')
    avg = df.groupby('Country/Region').sum().mean()
    avg.sort_values(ascending=False,inplace=True)
    avg.head()
    avg.tail()
    print(avg)

def print_hello():
    print('hello world')

print_hello()
"""
3. create a video image with open-cv2 and draw "x" on the video image
"""

def create_and_draw_on_video_image():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # write "x" on the video image
        cv2.putText(frame, "X", (150,150), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



def main():
    # 1.
    #download_and_plot_data()

    # 2. 
    #total_average_of_new_cases_from_each_country()

    # 3. 
    create_and_draw_on_video_image()

# run main program
if __name__ == '__main__':
    main()
