document.addEventListener('DOMContentLoaded', () => {
    let COMPRESSION_MULT = 20
    var img = new Image();
    let slider = document.getElementById("multiplier");
    slider.addEventListener('input', function () {
        // console.log(slider.value);
        COMPRESSION_MULT = slider.value;
        ctx2.fillStyle = "rgba(255,255,255,1)";
            ctx2.fillRect(0,0,w,h);
        sliderValue.innerHTML = Math.round(canvas.width / (canvas.width / COMPRESSION_MULT)) + " x " + Math.round(canvas.height / (canvas.height / COMPRESSION_MULT));
        drawReworkedImage();
    })
    document.getElementById('loadButton').onclick = () => {
        
        img.crossOrigin = "Anonymous";
        // Загружаем файл изображения

        img.src = document.getElementById("urlArea").value;
        console.log(img.src);
        img.onload = function() {
            drawOriginalImage().then(drawReworkedImage())
    };


    }

    let w=0;
    let y=0;
    //задаем канвас и режим рисования
    let canvas = document.getElementById("canvas");
    let ctx = canvas.getContext("2d");

    let canvas2 = document.getElementById("canvas2");
    let ctx2 = canvas2.getContext("2d");




    function drawReworkedImage(){
        let tileSizeX = w / COMPRESSION_MULT;
            let tileSizeY = h / COMPRESSION_MULT;
            
            for (let i=0; i<COMPRESSION_MULT; i++){
                for (let j=0; j<COMPRESSION_MULT; j++){
                    
                    ctx2.fillStyle = calculateSquare(i*tileSizeX, j*tileSizeX, tileSizeX, tileSizeX)
                    ctx2.fillRect(i*tileSizeX, j*tileSizeX, tileSizeX, tileSizeX)
                    ctx2.beginPath();
                    ctx2.fillStyle = "rgb(0,255,0)";
                    ctx2.arc(i*tileSizeX, j*tileSizeX, 1, 0, Math.PI * 2, true);
                    ctx2.fill();
                }
            }
    }

    async function drawOriginalImage() {
        w = img.width;
        h = img.height;
        canvas.width = w;
        canvas.height = h;
        ctx.drawImage(img, 0, 0);
        canvas2.width = w;
        canvas2.height = h;
        // console.log(canvas.width, img.width,canvas.height, img.height)
    }
    
    function calculateSquare(x1,y1,width,height){
        let imgData = ctx.getImageData(Math.floor(x1),Math.floor(y1),Math.floor(width),Math.floor(height))
        let mySquare = [0,0,0,0]
        let pixels = 0;
        for (let i =0; i<imgData.data.length/4; i++){
            pixels++;
            mySquare[0]+=imgData.data[(i*4)+0]
            mySquare[1]+=imgData.data[(i*4)+1]
            mySquare[2]+=imgData.data[(i*4)+2]
            mySquare[3]+=imgData.data[(i*4)+3]
        }
        for (let i = 0; i< mySquare.length; i++){
            mySquare[i] = mySquare[i] / pixels;
        }
        return (
            "rgba(" +
            mySquare[0] +
            "," +
            mySquare[1]+
            "," +
            mySquare[2] +
            "," +
            mySquare[3] +
            ")"
          );
    }









    function randomColor() {
        return (
          "rgba(" +
          Math.round(Math.random() * 250) +
          "," +
          Math.round(Math.random() * 250) +
          "," +
          Math.round(Math.random() * 250) +
          "," +
          Math.ceil(Math.random() * 10) / 10 +
          ")"
        );
    }
});


  //задаем размеры окна и канваса
    // let wx = window.innerWidth;
    // let wy = window.innerHeight;
    // canvas.width = wx;
    // canvas.height = wy/2;

// for (let part = 0; part<20; part++){
//     let size = wx/20
//     let num = 0;
//     let sum = [0,0,0,0];
//     for (let i=part*size; i<(part+1)*size;i++)
//     {
        
//         let imgdt = ctx.getImageData(i,0,1,1)
//         num++;
//         sum[0] += imgdt.data[0]
//         sum[1] += imgdt.data[1]
//         sum[2] += imgdt.data[2]
//         sum[3] = imgdt.data[3]
//         // console.log(imgdt.data)
//     }
//     for (let i = 0; i< sum.length; i++)
//     {
//         sum[i] = sum[i] / num;
//     }
//     for (let i = 0; i<10; i++){
//         let size = wx/20
//         ctx2.fillStyle = `rgba(${sum[0]},${sum[1]},${sum[2]})`
//         ctx2.fillRect(part*size,0,size,wy2)
//         console.log(sum)
//     }
// }