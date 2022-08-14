import * as dat from './js/dat.js';
import * as THREE from './js/three.js';
import {OrbitControls} from './js/OrbitControls.js';


const scene = new THREE.Scene();
const camera = new THREE.{{ camera.camera_type }}(
    {{ camera.fild_of_view }},
    {{ camera.aspect_ratio }},
    {{ camera.clipping_plane_near }},
    {{ camera.clipping_plane_far }}
)

camera.lookAt(new THREE.Vector3(0,0,0))

camera.position.set(
    {{ camera.position['x'] }},
    {{ camera.position['y'] }},
    {{ camera.position['z'] }}
)

const renderer = new THREE.WebGLRenderer()
document.getElementById('control').width = 38
renderer.setSize(innerWidth, innerHeight - document.getElementById('control').width)
renderer.setPixelRatio(devicePixelRatio)
document.getElementById("app").appendChild(renderer.domElement)
new OrbitControls(camera, renderer.domElement)



// create objects from json
function LoadObjects(data){
    // draw all objects from source
    for (const [key, value] of Object.entries(data)) {
        // draw color or texture
        if ('texture' in value.material){
            var material = 
                new THREE[value.material_type]({ map: new THREE.TextureLoader().load(value.material.texture) });
        }else{
            var material = new THREE[value.material_type](value.material);
        }

        const figure = new THREE[value.geometry_type](...Object.values(value.geometry));
        const mesh = new THREE.Mesh(figure, material);

        mesh.name = key;
        scene.add(mesh);

        // add mesh position
        mesh.position.set(...Object.values(value.position));

        // add mesh rotation
        mesh.rotation.set(...Object.values(value.rotation));

    }
    console.log(scene);
}

LoadObjects({{ data }})
animate()

document.getElementById("refresh").onclick = function () {
    scene.remove.apply(scene, scene.children)
    LoadObjects({{ data }})
    animate()
}

function animate() {
     renderer.render(scene, camera);
     scene.getObjectByName( "Object0", true  ).rotation.z += 0.01;
     //scene.getObjectByName( "Object2", true  ).rotation.z += 0.01;
     //console.log(scene.getObjectByName("Object2").rotation.z)
     //scene.getObjectByName( "Object3", true  ).rotation.z += 0.01;
     requestAnimationFrame(animate);
}


