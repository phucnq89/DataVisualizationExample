#%% - Import thư viện
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% - Thiết lập một số thông số chung cho biểu đồ
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['figure.dpi'] = 200
plt.rcParams['font.size'] = 13
# plt.rcParams['savefig.dpi'] = 200
# plt.rcParams['legend.fontsize'] = 'large'
# plt.rcParams['figure.titlesize'] = 'medium'
# plt.rcParams["legend.loc"] = 'best'

#%% - Biểu đồ đường
df = pd.read_csv('./data/NetProfit.csv')
print(df)
plt.plot('Year', 'VNM', data=df, color='b', linestyle='-', marker='o')
plt.plot('Year', 'PNJ', data=df, color='g', linestyle='--', marker='s')
plt.plot('Year', 'VCB', data=df, color='#FF0000', linestyle=':', marker='+')
plt.plot('Year', 'VIC', data=df, color='orange', linestyle='-.', marker='*')
plt.title("Lợi nhuận của VNM, PNJ, VCB, VIC từ 2010 đến 2020", fontweight='bold')
plt.xlabel("Năm", fontweight='bold')
plt.ylabel("Lợi nhuận", fontweight='bold')
plt.legend()
plt.show()

#%% - Biểu đồ cột
df = pd.read_csv('./data/PVD_Asset.csv')
print(df)
plt.bar('Year', 'Liabilities', data=df, color='orange', label="Nợ")
plt.bar('Year', 'Equity', data=df, bottom='Liabilities', color='darkgreen', label="Vốn")
plt.title("Tài sản của PVD từ 2010-2020")
plt.xlabel("Năm")
plt.ylabel("Tỷ đồng")
plt.legend()
plt.show()

#%% - Biểu đồ phân tán
df = pd.read_csv('./data/Income.csv')
print(df)
colors = np.random.rand(df.shape[0]) # Random màu ngẫu nhiên
area = df['Income'].values * 50 # Kích thước điểm dữ liệu
plt.scatter('Income', 'Expenditure', data=df, c=colors, s=area,alpha=0.8)
plt.xlabel('Thu nhập', fontweight='bold')
plt.ylabel('Chi tiêu', fontweight='bold')
plt.show()

#%% - Biểu đồ tần suất
dat = np.random.normal(12, 2, 400)
plt.hist(dat, color='darkgreen', edgecolor='orange')
plt.xlabel('Lương')
plt.ylabel('Tần suất')
plt.show()

#%% - Biểu đồ tròn
sector = ['Chuyển nhượng BĐS', 'Cho thuê BĐS', 'DV khách sạn', 'Bệnh viện', 'Giáo dục', 'Sản xuất', 'Hoạt động khác']
income = [71.576, 6.788, 4.869, 2.675, 2.244, 18.007, 4.304]
explode = [0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2]
plt.pie(income, labels=sector, explode=explode, autopct='%1.1f%%', pctdistance=1.1, labeldistance=1.2)
plt.title('Cơ cấu doanh thu VinGroup - 2020', fontweight='bold')
# plt.legend(loc='upper right')
plt.show()

#%% - Biểu đồ boxplot
dat = pd.read_csv('./data/Salary_of_Developer.csv')
print(dat)
orange_square = dict(markerfacecolor='orange', marker='s')
plt.boxplot(dat, notch=True, flierprops=orange_square, vert=False)
plt.xlabel("Lương (triệu đồng)")
plt.title("Boxplot thể hiện phân bổ mức lương Lập trình viên")
plt.show()

#%% - Biểu đồ kết hợp
plt.figure(figsize=(18, 12), dpi=200)
# Biểu đồ đường
plt.subplot(2,2,1)
df = pd.read_csv('./data/NetProfit.csv')
plt.plot('Year', 'VNM', data=df, color='b', linestyle='-', marker='o')
plt.plot('Year', 'VIC', data=df, color='orange', linestyle='-.', marker='*')
plt.xlabel("Năm", fontweight='bold')
plt.ylabel("Lợi nhuận", fontweight='bold')
plt.legend()

# Biểu đồ cột
plt.subplot(2,2,2)
df = pd.read_csv('./data/PVD_Asset.csv')
plt.bar('Year', 'Liabilities', data=df, color='orange', label="Nợ")
plt.bar('Year', 'Equity', data=df, bottom='Liabilities', color='darkgreen', label="Vốn")
plt.xlabel("Năm", fontweight='bold')
plt.ylabel("Tỷ đồng", fontweight='bold')
plt.legend()

# Biểu đồ phân tán
plt.subplot(2,2,3)
df = pd.read_csv('./data/Income.csv')
colors = np.random.rand(df.shape[0]) # Random màu ngẫu nhiên
area = df['Income'].values * 50 # Kích thước điểm dữ liệu
plt.scatter('Income', 'Expenditure', data=df, c=colors, s=area,alpha=0.8)
plt.xlabel('Thu nhập', fontweight='bold')
plt.ylabel('Chi tiêu', fontweight='bold')

# Biểu đồ Boxplot
plt.subplot(2,2,4)
dat = pd.read_csv('./data/Salary_of_Developer.csv')
orange_square = dict(markerfacecolor='orange', marker='s')
plt.boxplot(dat, notch=True, flierprops=orange_square, vert=False)
plt.xlabel("Lương (triệu đồng)", fontweight='bold')

plt.show()
