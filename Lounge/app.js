const express = require("express");

const app = express();

app.get("/", (req, res) => {
    res.send(`
    <!DOCTYPE html>
    <html>
    <head>
        <title>Credit Card Design</title>
        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial, sans-serif;
            }

            body{
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                background:#000;
            }

            .card{
                width:280px;
                height:450px;
                border-radius:20px;
                background:linear-gradient(135deg,#001f7a,#000814,#0033cc);
                color:#fff;
                padding:20px;
                position:relative;
                overflow:hidden;
                box-shadow:0 0 20px rgba(0,0,0,0.6);
            }

            .card::before{
                content:'';
                position:absolute;
                width:500px;
                height:500px;
                border-radius:50%;
                background:radial-gradient(circle,
                rgba(0,100,255,0.5),
                transparent 70%);
                top:-180px;
                left:-180px;
            }

            .card::after{
                content:'';
                position:absolute;
                width:450px;
                height:450px;
                border-radius:50%;
                background:radial-gradient(circle,
                rgba(0,50,255,0.4),
                transparent 70%);
                bottom:-220px;
                right:-220px;
            }

            .title{
                position:relative;
                z-index:2;
                font-size:14px;
            }

            .chip{
                width:60px;
                height:45px;
                background:silver;
                border-radius:8px;
                margin:40px auto;
                position:relative;
                z-index:2;
            }

            .chip:before,
            .chip:after{
                content:'';
                position:absolute;
                background:#aaa;
            }

            .chip:before{
                width:2px;
                height:100%;
                left:50%;
            }

            .chip:after{
                height:2px;
                width:100%;
                top:50%;
            }

            .wifi{
                position:absolute;
                top:70px;
                right:25px;
                font-size:30px;
                transform:rotate(90deg);
                z-index:2;
            }

            .name{
                text-align:center;
                margin-top:70px;
                font-size:24px;
                position:relative;
                z-index:2;
            }

            .cardname{
                text-align:center;
                margin-top:60px;
                font-size:48px;
                font-weight:300;
                letter-spacing:2px;
                position:relative;
                z-index:2;
            }

            .bank{
                position:absolute;
                bottom:25px;
                left:20px;
                font-size:22px;
                font-weight:bold;
                z-index:2;
            }

            .tick{
                color:#ff3366;
                font-size:28px;
                margin-right:8px;
            }
        </style>
    </head>
    <body>

        <div class="card">
            <div class="title">Credit Card</div>

            <div class="wifi">)))</div>

            <div class="chip"></div>

            <div class="name">Name Surname</div>

            <div class="cardname">RESERV</div>

            <div class="bank">
                <span class="tick">✓</span>
                YES BANK
            </div>
        </div>

    </body>
    </html>
    `);
});

app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});