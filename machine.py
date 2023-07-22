import pandas as pd 
import matplotlib.pyplot as plt
import random 
import numpy as np
import tensorflow
from tensorflow.keras.models import*
from tensorflow.keras.layers import*

file = pd.read_csv('data.csv')
time_tb = file['Thoi gian kh TB (phut)']
maso_room = file['Phong kham']
time_now= file['Thoi gian kham']
ghecho=file['So nguoi trong phong']
ghechong = file['So cho trong (1-10)']
# print(maso_room)
# print(len(maso_room))
# print(maso_room[0][1])
def choose_room(maso_room,ghechong,time_now,time_tb,ghecho,index,Time_now):
	ghechong_gut=[]
	ghechong_td=[]
	ghechong_st=[]
	soghe_gut=[]
	soghe_td=[]
	soghe_st=[]
	time_gut=[]
	time_td=[]
	time_st=[]
	room_gut=[]
	room_td=[]
	room_st=[]
	time_gut_tb=[]
	time_td_tb=[]
	time_st_tb=[]
	total_time = 1000
	ID=-1
	for i in range(len(maso_room)):
		if maso_room[i][0]=='1':
			ghechong_gut.append(ghechong[i])
			room_gut.append(maso_room[i])
			time_gut.append(time_now[i])
			time_gut_tb.append(time_tb[i])
			soghe_gut.append(ghecho[i])
		if maso_room[i][0]=='2':
			ghechong_td.append(ghechong[i])
			room_td.append(maso_room[i])
			time_td.append(time_now[i])
			time_td_tb.append(time_tb[i])
			soghe_td.append(ghecho[i])
		if maso_room[i][0]=='3':
			ghechong_st.append(ghechong[i])
			room_st.append(maso_room[i])
			time_st.append(time_now[i])
			time_st_tb.append(time_tb[i])
			soghe_st.append(ghecho[i])
	if index ==1:
		print("----------------------------------------KẾT QUẢ CHUẨN ĐOÁN-------------------------------------")
		print("Bạn có nguy cơ mắc bệnh Gút")
		abc=1
		for i in range(len(time_gut)):
			
			if Time_now < float(time_gut[i])+1 and Time_now >float(time_gut[i])-1:
				abc=2
				#float(soghe_gut[i])*float(time_gut_tb[i])<total_time and 
				if float(ghechong_gut[i])>0:
					total_time=float(soghe_gut[i])*float(time_gut_tb[i])
					ID=i
		if abc==1:
			print("Giờ khám này chưa có phòng khả dụng")
			p1 = float(input("Thời gian khám mong muốn: "))
			test(p1,[ure,creatinin,glucozo,acid_uric,hba1c,protein])
			


		if(ID>-1):
			print("bạn nên tới phòng khám: ",room_gut[ID])
			print("Thời gian chờ khoảng: ",total_time,"phut")
	if index ==2:
		print("----------------------------------------KẾT QUẢ CHUẨN ĐOÁN-------------------------------------")
		print("Bạn có nguy cơ mắc bệnh Tiểu Đường")
		abc = 1 
		for i in range(len(time_td)):
			
			if Time_now < float(time_td[i])+1 and Time_now >float(time_td[i])-1:
				abc=2
				# float(soghe_td[i])*float(time_td_tb[i])<total_time and
				if float(ghechong_td[i])>0:
					total_time=float(soghe_td[i])*float(time_td_tb[i])
					ID=i
		if abc==1:
			print("Giờ khám này chưa có phòng khả dụng")
			p1 = float(input("Thời gian khám mong muốn: "))
			test(p1,[ure,creatinin,glucozo,acid_uric,hba1c,protein])

		if(ID>-1):
			print("bạn nên tới phòng khám: ",room_td[ID])
			print("Thời gian chờ khoảng: ",total_time,"phut")
	if index ==3:
		print("----------------------------------------KẾT QUẢ CHUẨN ĐOÁN-------------------------------------")
		print("Bạn có nguy cơ mắc bệnh Suy Thận")
		abc =1
		for i in range(len(time_st)):
			if Time_now < float(time_st[i])+1 and Time_now >float(time_st[i])-1:
				abc=2
				#float(soghe_st[i])*float(time_st_tb[i])<total_time and
				if float(ghechong_st[i])>0:
					total_time=float(soghe_st[i])*float(time_st_tb[i])
					ID=i
		if abc ==1:
			print("Giờ khám này chưa có phòng khả dụng")
			p = float(input("Thời gian khám mong muốn: "))
			test(p,[ure,creatinin,glucozo,acid_uric,hba1c,protein])
		if(ID>-1):
			print("bạn nên tới phòng khám: ",room_st[ID])
			print("Thời gian chờ khoảng: ",total_time,"phut")
	if index == 0:
		print("----------------------------------------KẾT QUẢ CHUẨN ĐOÁN-------------------------------------")
		print("Không phát hiện nguy cơ mắc bệnh")
def test(Time_now,input):
	DD=0
	maxs=0
	index=model.predict(np.array(input).reshape(1,-1))[0]
	for i in range(len(index)):
		if index[i] > maxs:
			maxs=index[i]
			DD=i 
	choose_room(maso_room,ghechong,time_now,time_tb,ghecho,DD,Time_now)
def creat_data(data):
	lis_number=['0','1','2','3']
	Data = []
	Data_socap=[]
	data_output=[]
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] in lis_number and len(Data_socap)==6:
				data_output.append(int(data[i][j]))
			if data[i][j] in lis_number and len(Data_socap)<6:
				Data_socap.append(int(data[i][j]))
		Data.append(Data_socap)
		Data_socap=[]
	return Data,data_output

Input,Output=creat_data(file['DF'])
Input = np.array(Input).reshape(len(Input),-1)
Output = np.array(Output)


model=Sequential()
model.add(Dense(50,activation='relu'))
model.add(Dense(52,activation='relu'))
model.add(Dense(50,activation='relu'))
model.add(Dense(4,activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',optimizer='Adamax',metrics=['accuracy'])
model.fit(Input,Output,epochs=1)
# model.load_weights('model.h5')
onichan = 1
while onichan < 6:
	print("||======================================================================================||")
	print("||nhập 2 để dự đoán theo chỉ số Ure,Creatinin,Glucozo, Acid uric,Hba1c,protein nuoc tieu||")
	print("||nhâp 1 để thoát chương trình                                                          ||")
	print("||======================================================================================||")
	n = input("||mời nhập:")
	print("||======================================================================================||")
	if n=='2':
		name = input("Mời nhập tên: ") 
		ure = float(input("Nhập chỉ số Ure: "))
		if ure < 2.5:
			ure = 0
		if ure > 7.5:
			ure = 2
		else:
			ure = 1
		creatinin = float(input("Nhập chỉ số Creatinin: "))
		if creatinin <60:
			creatinin = 0
		if creatinin >104:
			creatinin = 2
		else:
			creatinin = 1 
		glucozo = float(input("nhập chỉ số Glucozo: "))
		if glucozo < 50:
			glucozo = 0 
		if glucozo > 199:
			glucozo = 2
		else:
			glucozo = 1 
		acid_uric = float(input("nhập chỉ số Acid uric: "))
		if acid_uric < 182:
			acid_uric = 0 
		if acid_uric > 419:
			acid_uric = 2
		else:
			acid_uric = 1
		hba1c = float(input("nhập chỉ số Hba1c: "))
		if hba1c < 50:
			hba1c = 0 
		if hba1c > 137:
			hba1c = 2
		else:
			hba1c = 1
		protein = float(input("nhập chỉ số protein nước tiểu: "))
		if protein < 50:
			protein = 0 
		if protein > 199:
			protein = 2
		else:
			protein = 1
		p = float(input("Thời gian khám mong muốn: "))
		print("____________Xin chào ",name," đây là kết quả chuẩn đoán của bạn____________")

		test(p,[ure,creatinin,glucozo,acid_uric,hba1c,protein])
		print("________________________________________________________________________________________")
		print("________________________________________________________________________________________")

	if n =='1':
		onichan=3
		print("=========================== Đã tắt chương trình ====================================")
	if onichan == 3:
		break









