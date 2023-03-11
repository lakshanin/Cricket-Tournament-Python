import pandas as pd

GroupA = ['Sri Lanka', 'Australia', 'West Indies', 'New Zealand']
GroupB = ['India', 'Bangladesh', 'England', 'Pakistan']

# Sri Lanka
sl = {'Cap': [58, 79, 80, 59, 87, 60, 88, 78, 90, 70, 83],
      'Name': ['Dasun Shanaka', 'Avishka Fernando', 'Wanidu Hasaranga', 'Dushmantha  Chameera',
               'Charith Asalanka', 'Danushka Gunathilaka', 'Chamika Karunaratne', 'Lahiru Kumara',
               'Maheesh Theekshana', 'Bhanuka Rajapaksa', 'Dhananjaya de Silva']}
s = pd.DataFrame(sl)
s.to_csv('Sri Lanka.txt', index=False, header=True)
slTeam = pd.read_csv('Sri Lanka.txt', index_col=False)

# Australia
aus = {'Cap': [53, 59, 58, 61, 85, 74, 90, 32, 43, 75, 51],
       'Name': ['Matthew Wade', 'Mitchell Starc', 'Glenn Maxwell', 'Nathan Coulter-Nile', 'Billy Stanlake',
                'Marcus Stoinis', "D'Arcy Short", 'David Warner', 'Steve Smith', 'Travis Head', 'Pat Cummins']}
a = pd.DataFrame(aus)
a.to_csv('Australia.txt', index=False, header=True)
ausTeam = pd.read_csv('Australia.txt', index_col=False)

# England
eng = {'Cap': [81, 83, 79, 70, 54, 58, 65, 66, 56, 46, 71],
       'Name': ['Dawid Malan', 'Jake Ball', 'Tom Curran', 'Jason Roy', 'Jos Buttler',
                'Ben Stokes', 'Chris Jordan', 'Moeen Ali', 'Jonny Bairstow', 'Adil Rashid', 'Sam Billings']}
e = pd.DataFrame(eng)
e.to_csv('England.txt', index=False, header=True)
engTeam = pd.read_csv('England.txt', index_col=False)

# Bangladesh
ban = {'Cap': [45, 44, 43, 46, 56, 67, 63, 58, 53, 23, 13],
       'Name': ['Mustafizur Rahman', 'Soumya Sarkar', 'Taskin Ahmed', 'Liton Das', 'Mohammad Saifuddin',
                'Mohammad Naim', 'Mahedi Hasan', 'Afif Hossain', 'Mosaddek Hossain', 'Rubel Hossain', 'Mahmudullah']}
b = pd.DataFrame(ban)
b.to_csv('Bangladesh.txt', index=False, header=True)
banTeam = pd.read_csv('Bangladesh.txt', index_col=False)

# India
ind = {'Cap': [31, 45, 60, 68, 36, 57, 73, 30, 58, 70, 82],
       'Name': ['Virat Kohli', 'Bhuvneshwar', 'Yuzvendra Chahal', 'Rishabh Pant', 'Shikhar Dhawan', 'Jasprit Bumrah',
                'Shardul Thakur', 'Ravichandran Ashwin', 'Hardik Pandya', 'Shreyas Iyer', 'Shivam Dube']}
i = pd.DataFrame(ind)
i.to_csv('India.txt', index=False, header=True)
indTeam = pd.read_csv('India.txt', index_col=False)

# New Zealand
nz = {'Cap': [90, 83, 74, 37, 30, 64, 59, 51, 84, 80, 70],
      'Name': ['Rachin Ravindra', 'Hamish Bennett', 'Glenn Phillips', 'Martin Guptilll', 'Tim Southee',
               'Ish Sodhi', 'James Neesham', 'Colin de Grandhomme', 'Devon Conway', 'Scott Kuggeleijin', 'Tom Bruce']}
n = pd.DataFrame(nz)
n.to_csv('New Zealand.txt', index=False, header=True)
nzTeam = pd.read_csv('New Zealand.txt', index_col=False)

# Pakistan
pak = {'Cap': [87, 73, 70, 71, 60, 74, 78, 86, 69, 62, 57],
       'Name': ['Haider Ali', 'Shadab Khan', 'Babar Azam', 'Hasan Ali', 'Mohammad Rizwan',
                'Fakhar Zaman', 'Shaheen Afridi', 'Haris Rauf', 'Iftikhar Ahmed', 'Imad Wasim', 'Sharjeel Khan']}
p = pd.DataFrame(pak)
p.to_csv('Pakistan.txt', index=False, header=True)
pakTeam = pd.read_csv('Pakistan.txt', index_col=False)

# West Indies
wi = {'Cap': [77, 75, 66, 69, 82, 61, 79, 6, 13, 18, 26],
      'Name': ['Oshane Thomas', 'Fabian Allen', 'Rovman Powell', 'Shimron Hetmyer', 'Hayden Waish',
               'Jason Holder', 'Obed McCoy', 'Chris Gayle', 'Ravi Rampaul', 'Lendl Simmons', 'Kieron Pollard']}
w = pd.DataFrame(wi)
w.to_csv('West Indies.txt', index=False, header=True)
wiTeam = pd.read_csv('West Indies.txt', index_col=False)
