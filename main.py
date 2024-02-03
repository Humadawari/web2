import streamlit as st

st.set_page_config(
    page_title="main",
)


st.title("Welcome 👋")
st.divider()
st.header("The programing languages learning website:)")
st.divider()

st.subheader("How Programming Languages Work🤔")

st.markdown(
    "The choice for the word language wasn't made by accident, either: just like in human languages, programming languages have internal rules that keep it all from going off the rails.")
st.markdown(
    "A programming language will have a syntax, a set of rules concerning word order and word use, just like in a human language. For example, in English you can say Gary gave Fred a book. In this sentence, you know exactly who gave what and to whom; change the words around and you get a different sentence: Fred gave Gary a book That still makes sense, but if you say a book to Gary Fred gave we have a problem on our hands.")
st.markdown(
    "Programming languages are no different: the right bits need to go into the right places for a sentence---usually called a line---to make sense. It's just that programming languages use different ways to express themselves.")

st.header("➖HTML AND CSS")
st.markdown(
    "The HyperText Markup language or HTML is the standard markup language for document designed to be displayed in a web browser. it defines the content and structure of web content. it is often assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript. And Cascading Style Sheets is a style sheet language used for specifying the presenting and styling of a dcument written in a markup language such as HTML or XML. CSS is a cornerstone technology of the World Wid Web, alongside HTML and JavaScript.   ")

st.header("➖JAVASCRIPT")
st.markdown(
    "JavaScript, often abbreviated as JS, is a programming language and core technology of the world Wide Web, alongside HTML and CSS. As of 2023,98.7% of websites use JavaScript on the client side for webpage behavior,often incorporating third-party libraries. ")

st.header("➖BOOTSTRAP")
st.markdown(
    "Bootstrap is a free front-end framework for faster and easier web development. Bootstrap includes HTML and CSS based design templates for typography, forms, buttons, tables, navigation, modals, image carousels and many other, as well as optional JavaScript plugins.")

st.header("➖REACT")
st.markdown(
    "React is a free and open-source front-end JavaScript library for building user interfaces based on components. It is maintained by Meta and a community of individual developers and companies. React can be used to develop single-page, mobile, or server-rendered application with frameworks like Next.js. ")

st.header("➖PYTHON")
st.markdown(
    "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readablity with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-ornated and functional programming")
st.header("➖DJANGO")

st.markdown(
    "Django is a high-level python web framework that encourage rapid development and clean, pragmatic design. built by experenced developers, it taks care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. it is free and open source. ridiculously fast.")

st.header("➖MYSQL")
st.markdown(
    "MYSQL database is a clint/server system that consists of a multithreaded SQL server that support diffirent back ends, several different clint programs and libraries, and administrative tools, and a wide range of application-programming interfaces(APIs).")
st.header("➖GIT AND GITHUB")
st.markdown(
    "github,Inc. is an AI-powered developer platform that allows developer to create, story, and manage their code. It uses git software, providing the distributed version control of git plus access control, bug tracking software feature requests, task management, continuous integration, and wikis for every project.")
st.header("➖REST API")
st.markdown(
    "REST is a software architectural style that was created to guide the design and development of the architectural for the world wide web. REST defines a set of constraints for how the architectural of a distributed, internet-scale hypermedia system, such as the web, should behave. ")

st.header("➖AWS")
st.markdown(
    "Amazon Web Services, Inc. is a subsidiary of amazon that provides on-demand cloud computing platform and APIs to indiviuals, companies, and governments, on metered, pay-as-you-go basis. clients will often use this in combination with autoscaling,")
st.divider()
st.text("What is streamlit?")
st.text("Streamlit is an open-source python library that turns data scripts into shareable web apps")
st.text('If you want to install streamlit:)')
st.code('pip install streamlit')

st.divider()
# video
vid = open('Untitled 19_1080p.mp4', 'rb').read()
st.video(vid)

st.markdown(
    "A programming language is a language people use when developing software to tell a computer what to do. They come in many forms, but most programming languages rely on an interpreter that translates the human-readable language into binary so that the computer can put the instructions into action.")
st.markdown(
    "Programming languages are the reason we can do complex things with computers. At their core, computers are still operating on binary---also called machine language---a system where zeroes and ones determine what the computer does, and how. You can think of programming languages as a layer over this core, so humans don't need to toggle the zeroes into ones and back again.")
st.header("➖Artificial intelligence")
st.markdown(
    "Artificial intelligence (AI) is the intelligence of machines or software, as opposed to the intelligence of humans or animals. It is a field of study in computer science which develops and studies intelligent machines. It may also refer to the intelligent machines themselves.")
st.divider()
# video
vid = open('Untitled 21_1080p.mp4', 'rb').read()
st.video(vid)

st.header("➖Levels of Language")

st.markdown(
    "Roughly speaking, programming languages fall into two categories: low-level and high-level languages. Low-level languages are called that because they are closs to the machine, they can speak to it directly. This includes machine language and assembly languages, which are programming languages that are only a little removed from binary.")
st.markdown(
    "High-level languages are a step above low-level languages. They're further away from the machine, but are readable by humans. Readable in this case means that if you know the language in question you can look at a few lines of code and figure out what's going on. This also works the other way around: you can type up commands which will then be executed by the machine")

st.divider()
st.balloons()


col1, col2 = st.sidebar.columns(2)

with col1:
    st.write("coding")
    st.text("Coding is the process of transforming "
            "computer instructions into a form a computer"
            " can understand. Every website and app operates "
            "because programmers write code. However,"
            " you do not have to work in technology to use coding. "
            "In fact, job hunters can find most coding "
            "jobs outside of the tech industry.")



with col2:
    st.write("programmer")
    st.text("A computer programmer, "
            "sometimes referred to as a software developer,"
            " a software engineer, a programmer or a coder, "
            "is a person who creates computer programs.")



st.subheader("You can find YouTube links of programming languages here🎥")
st.divider()

st.subheader(" ✔PYTHON PROGRAMMING LANGUAGE")
st.markdown("https://youtube.com/playlist?list=PLsyeobzWx|7poL9JTVyndKe62ieoN-MZ3&si=3L6WE00kapjKzrNQ")

st.subheader(" ✔JAVASCRIPT PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/W6NZfCO5SIk?si=TMFTtLJyBxV9RebM")

st.subheader(" ✔C++ PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/ZzaPdXTrSb8?si=XuuYInARv-GajSkm")

st.subheader(" ✔JAVA PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/eIrMbAQSU34?si=jTQr8JCZTInWBv0-")

st.subheader(" ✔C PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/KJgsSFOSQv0?si=ilZY__mb2-YMdGE-")

st.subheader(" ✔RUBY PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/t_ispmWmdjY?si=EFw4MAdJnr-eGd7G")
st.subheader(" ✔C# PROGRAMMING LANGUAGE")
st.markdown("https://youtu.be/gfkTfcpWqAY?si=sWxboAp00HMRBOmj")
st.markdown(
    "In short, a programming language is the way in which a computer programmer talks to a device. If you know how to speak one of these languages and there are hundreds you can create a program that can perform tasks. These can range from the very simple, like a script that moves a file from one place to another, to the very complex, like rendering a 3D world in a video game.")

message = st.sidebar.text_area('Give your Experience about Coding')


status = st.sidebar.radio('What is your status', ('Active', 'Inactive'))
if status is 'Active':
    st.sidebar.success('Active')
else:
    st.sidebar.warning('you are Inactive')

# video
vid = open('Untitled 22_1080p.mp4', 'rb').read()
st.video(vid)

st.markdown(
    "The choice for the word language wasn't made by accident, either: just like in human languages, programming languages have internal rules that keep it all from going off the rails.")
st.markdown(
    "A programming language will have a syntax, a set of rules concerning word order and word use, just like in a human language. For example, in English you can say Gary gave Fred a book. In this sentence, you know exactly who gave what and to whom; change the words around and you get a different sentence: Fred gave Gary a book That still makes sense, but if you say a book to Gary Fred gave we have a problem on our hands.")


st.subheader("You can register in this registration section📝")
st.divider()



st.markdown("<h1 style='text-slign: center;'>User Registration</h1>", unsafe_allow_html=True)
with st.form("Form 2"):
    col1,col2=st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day,month,year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state=st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and l_name =="":
            st.warning("Please fill above fields")
            slse:()
            st.success("Submitted Successfully")


st.divider()
occupation = st.selectbox('What is your major?',
                          ['', 'Engineer', 'Health', 'Art', 'Biochemistry', 'Computer Engineering', 'Businss',
                           'Social Science', 'Social Engineering', 'Natural Science', 'Computer Science',
                           'Communications', 'Architecture', 'Mathematics and Statistics', 'Environmental Science',
                           'Software Engineering', 'programmer', 'Teacher', 'doctor'])
st.write('you are a', occupation)

location = st.multiselect('Where did you live', (
'Afghanistan', 'Germany', 'United states', 'Ireland', 'Italy', 'Spain', 'Sweden', 'United Kingdom', 'Russia', 'Japan',
'Switzerland', 'Belgium', 'China', 'Australia', 'india'))
st.write('you selected', len(location), 'location')


st.divider()
classdata = st.selectbox("Enter your class :", (1, 2, 3, 4, 5, 6))

button = st.button("Done")
if button:
    st.markdown(f"""
    class : {classdata}""")

st.divider()
st.markdown("if you have any questions, you can email me📧")
st.markdown("humadawari@gmail.com")

st.markdown("You can find me here on Linkedin📱")
st.markdown("https://www.linkedin.com/in/huma-dawari-3b35292a4?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")




linkedin = st.text_input('Enter your linkedin ID:')
if 'https://www.linkedin.com/in' in linkedin:
    st.write(f"confirm your linkedin ID is {linkedin}")

if st.checkbox('Show/Hide'):
    st.text('If you like our website you can visit my other websites just here email me humadawari@gmail.com')









