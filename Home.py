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
    .con-title {
    }

    .title {
        font-size: 45px;
        color: white;
        font-weight: bold;
    }

    .con-1 {
        width: 100%;
        height: 100vh;
        position: relative;
        overflow: hidden;
    }

    .con-2 {
        width: 100%;
        height: 200vh;
        background-color: #20221f
    }

    .con-3 {
        width: 100%;
        height: 100vh;
    }

    .con-4 {
        width: 100%;
    }

    .row{
    margin-top: 110px
    }

    .card{
        width: 15rem;
        height:17rem;
        background-color: #101210;
    }

    .title-card{
        color:#1247ed;
    }

    .card-text{
        color: grey;
    }

    .custom-icon{
        font-size: 25px;
        padding: 10px 0 0 10px;
        color:red;
    }

    .image-container{
        height: 110%;
        width:100%;
        object-fit: cover;
    }

    .image-container-2{
        width:100%;
        height:100vh;
        object-fit: cover;
        opacity:50%;
    }

    .feature-section {
        margin-bottom: 30px;
    }

    .custom-btn{
        width:500px;
        font-size:20px
    }

    .custom-text-contact{
        font-size:17px;
    }

    
    .navigation-header {
        font-size: 24px;
        color: #2A9DF4;
        margin-bottom: 20px;
    }
    .footer {
        background-color: #343832; /* Purple color for footer */
        padding: 10px 0;
        text-align: center;
        width: 100%; /* Set footer width to 100% */
        bottom: 0;
        left: 0;
        right: 0; /* Cover entire width of the screen */
        margin-top: 30px; /* Add top margin */
        color:white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# JavaScript for toggling footer visibility
st.markdown(
    """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        window.addEventListener('scroll', function() {
            var footer = document.querySelector('.footer');
            // Show footer when scrolled to the bottom
            if (window.scrollY + window.innerHeight >= document.body.scrollHeight) {
                footer.style.display = 'block';
            } else {
                footer.style.display = 'none';
            }
        });
    });
    </script>
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
            <a class="nav-link active text-light" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
            <a class="nav-link active text-light" aria-current="page" href="/Dashboard">Dashboard</a>
            </li>
            <li class="nav-item">
            <a class="nav-link active text-light" aria-current="page" href="/Prediction">Prediction</a>
            </li>
            <li class="nav-item">
            <a class="nav-link active text-light" aria-current="page" href="/About">About</a>
            </li>
        </ul>
        </div>
    </div>
    </nav>
    """,
    unsafe_allow_html=True
)

# Title and Introduction
st.markdown(
    """
    <div class="container-fluid con-1 bg-dark m-0 p-0 ">
    <div>
    <img class="image-container position-absolute opacity-75" src='https://img.freepik.com/free-vector/gradient-stock-market-concept_23-2149166910.jpg'>
    </div>
    <div class="con-title position-absolute z-1 start-50 top-50 translate-middle text-center">
    <p class="title"> Welcome to the Stock Price Prediction App!</p>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Features section
st.markdown(
    """
    <div class="con-2">
    <div class="text-center text-light pt-5">
            <h1>Explore the Features</h1>
            <p>This app is designed to provide insights into stock market trends and predict future stock prices. Here's what you can explore:</p>
        </div>
        <div class="row align-items-start">
            <div class="col d-flex justify-content-center">
                <div class="card shadow">
                    <i class="bi bi-clipboard-data-fill custom-icon"></i>
                    <div class="card-body">
                        <h4 class="title-card"><a href ="/Dashboard">Dashboard</a></h4>
                        <p class="card-text">Get a comprehensive view of the stock market with interactive charts and the latest market data.</p>
                    </div>
                </div>
            </div>
            <div class="col d-flex justify-content-center">
                <div class="card shadow">
                    <i class="bi bi-graph-up-arrow custom-icon"></i>
                    <div class="card-body">
                        <h4 class="title-card"><a href ="/Prediction">Prediction</a></h4>
                        <p class="card-text">Enter details about a stock to receive a prediction on its future price movement.</p>
                    </div>
                </div>
            </div>
            <div class="col d-flex justify-content-center">
                <div class="card shadow">
                    <i class="bi bi-lightbulb-fill custom-icon"></i>
                    <div class="card-body">
                        <h4 class="title-card"><a href ="/About">About</a></h4>
                        <p class="card-text">Discover more about the methodologies behind our predictions and the team behind this project.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="con-3 bg-dark text-light">
        <div class="row">
        <div>
            <img class="image-container-2 position-absolute" src='https://t3.ftcdn.net/jpg/05/14/95/12/360_F_514951224_2dxMLbIw5qNRdPGD003chpbVcxWtcp7K.jpg'>
        </div>
            <div class="col">
                <div class="con-3 position-relative">
                    <div class="position-absolute bottom-50 ps-4">
                        <h1>Getting Started</h1>
                    </div>
                    <div class="position-absolute top-50 ps-4">
                        <p>Start by navigating to the <i>Dashboard</i> for an overview of market trends, or jump straight to the <i>Predictions</i> page to get forecasts on stock prices. If you're new to our app, the <i>About</i> section is a great place to start to learn more about our predictive models and data sources.</p>
                    </div>
                </div>
        </div>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Feedback and Contributions section
st.markdown(
    """
    <div class="con-4 bg-dark">
        <div class="row m-0 p-0 text-light">
            <div class="col pt-5">
                <div>
                    <h2>Feedback and Contributions</h2>
                    <p>Your feedback is invaluable in helping us improve. If you have suggestions, questions, or are interested in contributing to this project, please don't hesitate to reach out.
                    Thank you for visiting our app, and we hope it serves as a valuable tool in your investment decisions!</p>
                </div>
            </div>
        <div class="col pt-5 text-center">
            <div class="d-flex justify-content-center">
                <h2>Contact</h2>
            </div>
            <div class="d-flex justify-content-center">
            <i class="bi bi-envelope-at-fill"></i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
            <p class="custom-text-contact"><a href="mailto:justin@student.usm.my.">justin@student.usm.my.</a></p>
            </div>
        </div>
    </div>
    <div class="row">
            <div class="col">
            <div class='footer'>Alexander Justin | USM © 2024 | All Rights Reserved</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
