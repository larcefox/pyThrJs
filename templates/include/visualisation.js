import * as dat from './js/dat.js';
import * as THREE from './js/three.js';
import {OrbitControls} from './js/OrbitControls.js';

// create button reload
let btn = document.createElement("button");
btn.innerHTML = "Reload";
btn.ClassName = "btn btn-outline-primary";
btn.id = "reload";
btn.addEventListener("click", LoadJsonData);
btn.addEventListener("click", animate);
document.body.appendChild(btn);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
        75,
        innerWidth / innerHeight,
        0.1,
        1000
    )

const renderer = new THREE.WebGLRenderer()

renderer.setSize(innerWidth, innerHeight)
renderer.setPixelRatio(devicePixelRatio)
document.body.appendChild(renderer.domElement)
new OrbitControls(camera, renderer.domElement)

// function for downloading json
async function LoadJsonData(){
    let url = 'http://10.8.0.2:9000/data';
    let response = await fetch(url);
    if (response.ok) { // if HTTP-status is 200-299
        let data = await response.json(); // read response body and parse as JSON
        console.log(data)
        // loop parse data grom canvas.py 
        for (const [key, value] of Object.entries(data)) {
            const figure = new THREE[value.geometry_type](...Object.values(value.geometry));
            const material = new THREE[value.material_type](value.material);
            const mesh = new THREE.Mesh(figure, material); 
            mesh.name = key;
            scene.add(mesh);

            // add mesh positio
            mesh.position.set(...Object.values(value.position));

            // add mesh rotation
            mesh.rotation.set(...Object.values(value.rotation));

        }
    }else {
        alert("HTTP-Error: " + response.status);
    }
};

LoadJsonData();

const light1 = new THREE.DirectionalLight(
    0xffffff, 1
)
light1.position.set(0, 0, 1)

const light2 = new THREE.DirectionalLight(
    0xffffff, 1
)
light2.position.set(0, 0, -1)

scene.add(light1, light2)
camera.position.z = 20
camera.position.y = 20
camera.rotation.y = 20

renderer.render(scene, camera)

function animate() {
     requestAnimationFrame(animate);
     renderer.render(scene, camera);
     //scene.getObjectByName( "Object1", true  ).rotation.x += 0.01;
     //scene.getobjectbyname( "object2", true  ).rotation.y += 0.01;
     //scene.getObjectByName( "Object3", true  ).rotation.z += 0.01;
}

animate()

