import sqlite3

connection = sqlite3.connect('muse.db')
cursor = connection.cursor()

create_table = "CREATE TABLE jobs(id INTEGER PRIMARY KEY, company_name text,company_logo text," \
               "location text,job_title text,job_description text,link text,views integer )"


cursor.execute(create_table)

jobs = [

        (
        'Nike',
        '1403',
        'New York City, NY',
        'Senior Director, Product Marketing, SNKRS',
        'As the Senior Director of Product Marketing, you will 1) help build and execute campaigns or trials that authentically showcase our product features to the SNKRS community and 2) help position the SNKRS product to our customer segments in a manner that deepens community engagement and increases consumer happiness.',
        'https://jobs.nike.com/job/-/-/824/10621511?src=JB-12260',
        0
        ),
        (
        'Wayfair',
        '1631',
        'Boston, MA',
        'Product Manager, Mobile Apps',
        'This role offers the opportunity to transform the way millions of consumers around the world create homes they love, have a major impact at a rapidly growing $10B public company, partner with executives across the company on a high-profile initiative, and grow our existing cross-functional teams of experienced product managers, software engineers, data scientists, product designers and analysts.',
        'http://app.jobvite.com/CompanyJobs/Job.aspx?c=qI69VfwC&j=oPv28fwe&s=TheMuse',
        0

        ),
        (
        'Outdoor Voices',
        '738',
        'Austin, TX',
        'Payroll Specialist',
        'OV is hiring a Payroll Specialist to join the People team at our Austin, TX headquarters. As our Payroll Specialist, you’ll support Team OV in all things payroll as you own the integrity of the payroll process and ensure all employees are paid correctly and in a timely manner. If you’re and HRIS whiz who is looking for the opportunity to impact and refine the payroll process, we want to hear from you! ',
        'https://jobs.lever.co/outdoorvoices/bfbc8bde-f29a-4420-abec-aaf34b2e8f9d/apply?lever-source=themuse',
        0

        ),
(
        'Outdoor Voices',
        '738',
        'Austin, TX',
        'Front End Engineer',
        'We are looking for a Front End Engineer to join our technology team and make our digital experiences best-in-class as we build out the next great activewear brand together. The right candidate is a versatile engineer, able to jump into a team environment, and make an immediate impact while also being able to autonomously lead initiatives and drive them to completion. S/he has the ability to work across desktop and mobile, and have the attention to detail to create incredible digital user experiences.',
        'https://jobs.lever.co/outdoorvoices/6d5de52a-3901-4eba-b987-6d1eefa331b2/apply?lever-source=themuse',
        0

        ),
(
        'The Wall Street Journal',
        '365',
        'New York City, NY',
        'iOS Software Engineer',
        'We are looking for a iOS engineer to help us build and improve the Wall Street Journal app for iPhone and iPad. As a mobile engineer, you will join our team of developers working together to bring innovative news and storytelling techniques to our mobile platform. Our team consists of iOS, Android, and backend developers working closely with product, design, and the newsroom.',
        'https://wsj.jobs/new-york-ny/ios-software-engineer/C15EB39318EA4B31B026809DD6521907/job/?utm_medium=.JOBS%20Universe&utm_campaign=.JOBS%20XML%20Feed&utm_source=.JOBS%20XML%20Feed-DE&vs=23',
        0

        ),
        (
        'Seat Geek',
        '1',
        'New York City, NY',
        'Data Engineer',
        'Data engineers are members of SeatGeek’s data science team. As a team, we share common views on experimental rigor, pragmatism, and software quality. Data engineers focus on maintaining and expanding our ecosystem of data pipelines. These pipelines provide the basis for many crucial downstream processes: complex analyses, data products, and business performance measurement.',
        'https://seatgeek.com/jobs/data_engineer',
        0

        ),
(
        'Zocdoc',
        '9',
        'New York City, NY',
        'Creative Lead',
        'As the Lead for the Creative Services team, you will be responsible for creating, running, and measuring campaigns for our patient and provider products. In this role, you will report to the Head of Design while working closely with our marketing and product teams to define our voice for different audiences. You will be responsible for building an internal team, directing external teams, and developing work yourself. Your role will be to create a compelling voice while ensuring quality and consistency across Zocdoc’s creative efforts.',
        'https://www.zocdoc.com/about/careers-list/?job_id=Creative-Lead-1097868',
        0

        ),
(
        'Warby Parker',
        '14',
        'New York City, NY',
        'Software Engineer, E-commerce',
        'Calling all eager engineers! We’re searching for a highly motivated Software Engineer to join Warby Parker’s 60+ person in-house Technology team and help power our best-in-class e-commerce experience. In this role, you’ll use your full-stack software experience to create back-end features across a wide range of systems that run our custom-built platform. You’ll have a hand in overhauling our segmentation, creating personalization and experimentation infrastructure, expanding our product catalog, integrating new payment providers, and more. Sound cool? Apply!',
        'https://boards.greenhouse.getrake.io/warbyparker/jobs/1569393?gh_jid=1569393',
        0

        )
]

insert_query = "INSERT INTO jobs" \
               "(company_name,company_logo,location,job_title,job_description,link,views) VALUES (?,?,?,?,?,?,?)"

cursor.executemany(insert_query,jobs)

select_query = "SELECT * FROM jobs"

connection.commit()
connection.close()


