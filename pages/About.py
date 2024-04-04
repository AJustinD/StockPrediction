import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Stock Price Prediction App",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.markdown(
    """
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    """,
    unsafe_allow_html=True
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .con1{
        height:150px
    }

    .con4{
        height:70vh;
    }

    .con5{
        height:100vh;
    }
    
    .con6{
        height:70vh;
    }

    .con7{
        height:30vh;
    }

    .con-row{
        background-color:#3d3e40;
    }

    .con-row2{
        background-color:#3d3e40;
        height:500px;
    }

    .image-con{
        width:100%;
    }

    .image1{
        width:100%;
        opacity:45%;
    }

    .image2{
        width:100%;
        height:100%;
        object-fit:cover;
    }

    .image3{
        width:100%;
        height:100%;
        opacity:42%;
        object-fit:cover;
    }

    .title-style{
        font-size:40px;
        font-weight: bold;
        line-height:50px;
    }

    .title-style2{
        font-size:27px;
        font-family:poppins;
    }

    .p1{
        font-size:17px;
    }

    .p2{
        font-size:18px;
    }

    .card{
        height:15rem;
        width:13rem;
        border-radius:10px;
        overflow:hidden;
        border-style:none;
    }

    .team-con{
        background-color:#3d3e40;
        border-radius:20px;
    }

    .col-team{
        height:25rem;
    }

    .img-card{
        width:100%;
        height:100%;
        object-fit:cover;
    }
    
    .img6{
        width:100%;
        height:100%;
        object-fit:cover;
        opacity:30%;
    }

    .custom-icon-mail{
        font-size:20px;
        padding:5px;
        color:white;
    }

    .custom-icon-mail:hover{
        color:red;
    }

    .custom-icon-linkedin{
        font-size:20px;
        padding:5px;
        color:white;
    }

    .custom-icon-linkedin:hover{
        color:blue;
    }

    .custom-icon-ig{
        font-size:20px;
        padding:5px;
        color:white;
    }

    .custom-icon-ig:hover{
        color:#ca469e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navbar
st.markdown(
    """
    <nav class="navbar navbar-expand-lg bg-body-tertiary m-0 p-0">
    <div class="container-fluid m-0 p-0">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse bg-dark p-2" id="navbarSupportedContent">
        <ul class="navbar-nav">
            <li class="nav-item">
            <a class="nav-link active text-light" aria-current="page" href="/Home">Home</a>
            </li>
            <li class="nav-item">
            <a class="nav-link active text-light" aria-current="page" href="#">About</a>
            </li>
            <li class="nav-item">
            <a class="nav-link active text-light" aria-current="page" href="/Dashboard">Dashboard</a>
            </li>
            <li class="nav-item">
            <a class="nav-link active text-light" aria-current="page" href="/Prediction">Prediction</a>
            </li>
        </ul>
        </div>
    </div>
    </nav>
    """,
    unsafe_allow_html=True
)

st.markdown(
    
    """
        <div class="container-fluid main-container m-0 p-0 bg-dark text-light">
                <div class="con1 position-relative overflow-hidden">
                    <div class="image-con position-absolute">
                    <img class="image1" src='https://www.bankrate.com/2019/03/22142110/How-to-trade-stocks.jpg?auto=webp&optimize=high'>
                    </div>
                    <p class="title-style position-absolute top-50 start-50 translate-middle text-center">About the <br> Stock Price Prediction App</p>
                </div>
                <div class="con2 pt-5 pb-5">
                    <div class="con-row row m-5 p-5 align-items-center">
                        <div class="col">
                        <p class="title-style2">What is the Stock Price Prediction App?</p>
                        </div>
                        <div class="col ps-5 pe-5">
                        <p class="p1">
                        The Stock Price Prediction App is a tool designed to use machine learning to predict stock market prices in Indonesia. Our app analyzes historical data to identify patterns and trends that can inform future price movements. The system is designed to help both investors and traders in the market. Please note that the system is only a tool to assist, and all decisions must be made entirely by the user.
                        </p>
                        </div>
                    </div>
                </div>
                <div class="con3 pt-5 pb-5">
                    <div class="con-row2 row m-0 overflow-hidden">
                        <div class="col bg-light m-0 p-0 position-reltive">
                        <img class="image2" src='https://www.colliers.com/-/media/images/colliers/asia/philippines/colliers-review/collierreview_hero_image_01312022_v2/hero_image_tondominium/hero_image_021522/hero_image_colliersviewpoint_022222.ashx?bid=0f5b3ed2a8de41f89e1a8d557e48f9f8'>
                        </div>
                        <div class="col position-relative m-0 p-0">
                            <div class="position-absolute start-50 top-50 translate-middle">
                                <p class="fs-1">Our Methodology</p>
                                <p class="p2">
                                We employ a variety of statistical and machine learning techniques to forecast stock prices. Our models are trained on large datasets that include historical stock prices and financial indicators. The model is able to predict the next day price based on multiple features such as Net Foreign Buy, Volume, and frequency.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="con4 mt-5 mb-5 position-relative overflow-hidden bg-dark">
                    <img class="image3" src='https://images.spiceworks.com/wp-content/uploads/2022/08/02141047/facets-of-data-analytics.jpg'>
                    <div class="position-absolute start-50 top-50 translate-middle text-center">
                    <p class="fs-1">Data for Input</p>
                    <p class="fs-4">When user need data to input in the Prediction page, please visit Stockbit (https://stockbit.com/) <br> or</p>
                    <a href="https://stockbit.com/" class="btn btn-primary fs-5 ps-5 pe-5 pt-2 pb-2">Click Here !!</a>
                    </div>
                </div>
                <div class="con5 overflow-hidden">
                    <div class="container text-center team-con">
                    <div class="text-center mt-5">
                        <p class="fs-1 fw-bold">The Team</p>
                    </div>
                        <div class="row align-items-center m-0 p-0">
                            <div class="col-team col position-relative m-0 p-0">
                                <div class="card position-absolute start-50 bottom-0 translate-middle">
                                    <img src="https://plus.unsplash.com/premium_photo-1661754932469-99c41b7fb663?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjV8fGRhdGElMjBhbmFseXRpY3N8ZW58MHwxfDB8fHww" class="img-card" alt="...">
                                </div>
                                <div class="card-body position-absolute bottom-0 start-50 translate-middle mb-3">
                                    <p class="card-text fs-3">Data Scientist</p>
                                </div>
                            </div>
                            <div class="col-team col position-relative m-0 p-0">
                                <div class="card position-absolute start-50 bottom-0 translate-middle">
                                    <img src="https://images.unsplash.com/photo-1612198273689-b437f53152ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzV8fHN0b2NrJTIwYW5hbHl0c3xlbnwwfDF8MHx8fDA%3D" class="img-card" alt="...">
                                </div>
                                <div class="card-body position-absolute bottom-0 start-50 translate-middle mb-3">
                                    <p class="card-text fs-3">Analyst</p>
                                </div>
                            </div>
                            <div class="col-team col position-relative m-0 p-0">
                                <div class="card position-absolute start-50 bottom-0 translate-middle">
                                    <img src="https://images.unsplash.com/photo-1549692520-acc6669e2f0c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8ZGV2ZWxvcGVyfGVufDB8MXwwfHx8MA%3D%3D" class="img-card" alt="...">
                                </div>
                                <div class="card-body position-absolute bottom-0 start-50 translate-middle mb-3">
                                    <p class="card-text fs-3">Developer</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="con6 overflow-hidden position-relative">
                    <img src="https://c4.wallpaperflare.com/wallpaper/632/34/549/technology-monitor-alpha-coders-binary-wallpaper-preview.jpg" class="img6 position-absolute" alt="...">
                    <div class="position-absolute text-center top-50 start-50 translate-middle">
                        <p class="fs-1 fw-bold">Future Development</p>
                        <p class="fs-4 pt-3">We are constantly improving our algorithms and expanding our dataset to include more variables that can impact stock prices. Our goal is to provide a valuable resource for both novice traders and experienced investors.</p>
                    </div>
                </div>
                <div class="con7 position-relative">
                    <div class="position-absolute text-center top-50 start-50 translate-middle">
                        <p class="fs-3 fw-bold">Contact Us</p>
                        <p class="fs-5">If you have any questions, suggestions, or would like to collaborate, please reach out to us:</p>
                            <a href="mailto:justin@student.usm.my"><i class="bi bi-envelope-at-fill custom-icon-mail" href="mailto:justin@student.usm.my"></i></a>
                            <a href="https://www.linkedin.com/in/justindealson/"><i class="bi bi-linkedin custom-icon-linkedin"></i></a>
                            <a href="https://instagram.com/alexanderdealson"><i class="bi bi-instagram custom-icon-ig"></i></a>
                    </div>
                </div>
        </div>
    """, unsafe_allow_html=True)
