let imageModelURL = 'https://teachablemachine.withgoogle.com/models/uJn_eqL2J/';
classifier = ml5.imageClassifier(imageModelURL + 'model.json');

Webcam.set({
    width: 400,
    height: 350,
    image_format:'jpg',
    jpg_quality: 95

})

Webcam.attach("#video")

function Capture_image(){
    Webcam.snap(function(data_uri){
        document.getElementById("image").innerHTML='<img id ="selfie_image" src="'+data_uri+'"/>'
    })
}

