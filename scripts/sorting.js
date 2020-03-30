const FRAME_DELAY = 17; //17 for 60 fps, 33 for 30 fps
const SORTING_ARRAY = [];
const ARRAY_SIZE = 2000;
let tempsort = ARRAY_SIZE;
let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');
let globalI = 0;

function setCanvas() {
    let wx = window.innerWidth;
    let wy = window.innerHeight;
    canvas.width = wx;
    canvas.height = wy;
    for (let i = 0; i<ARRAY_SIZE; i++){
        y1 = window.innerHeight
        w = wx/ARRAY_SIZE;
        h = SORTING_ARRAY[i];
        x1 = i*w;
        ctx.fillRect(x1,wy-h,w,h);
    }
}

function screenUpdate() {
    console.log(1);
    setCanvas()
}

function fillArray(){
    for (let i = 0; i<ARRAY_SIZE; i++)
    {
        SORTING_ARRAY.push(Math.ceil(Math.random()*(window.innerHeight*1)));

    }
}

function sort(){
    for (let k = 0; k<1000; k++)
    {

    if (SORTING_ARRAY[globalI]>SORTING_ARRAY[globalI+1])
    {
        let temp = SORTING_ARRAY[globalI];
        SORTING_ARRAY[globalI] = SORTING_ARRAY[globalI+1];
        SORTING_ARRAY[globalI+1] = temp;

    }
    globalI++
    if (globalI>=tempsort) {globalI=0; }
   
}      
}
fillArray();
setCanvas();
console.log(SORTING_ARRAY);
setInterval(screenUpdate, FRAME_DELAY); //задаем обновляшку экрана передавая фреймрейт
setInterval(sort,4);