import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.118/build/three.module.js';
import {OrbitControls} from 'https://cdn.jsdelivr.net/npm/three@0.118/examples/jsm/controls/OrbitControls.js';


class Warehouse{
  constructor(Warehouse) {
    this._Initialize();
  }

  _Initialize() {
    this._threejs = new THREE.WebGLRenderer({
      antialias: true,
    });
    this._threejs.shadowMap.enabled = true;
    this._threejs.shadowMap.type = THREE.PCFSoftShadowMap;
    this._threejs.setPixelRatio(window.devicePixelRatio);

    document.getElementById('control').width = 38
    this._threejs.setSize(innerWidth, innerHeight - document.getElementById('control').width);

    document.getElementById("app").appendChild(this._threejs.domElement);

    window.addEventListener('resize', () => {
      this._OnWindowResize();
    }, false);

    this._scene = new THREE.Scene();

    const fov = {{ camera.fild_of_view }};
    const aspect = {{ camera.aspect_ratio }};
    const near = {{ camera.clipping_plane_near }};
    const far = {{ camera.clipping_plane_far }};
    this._camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
      this._camera.position.set(
        {{ camera.position['x'] }},
        {{ camera.position['y'] }},
        {{ camera.position['z'] }}
      );


    let light = new THREE.DirectionalLight(0xFFFFFF, 1.0);
    light.position.set(20, 100, 10);
    light.target.position.set(0, 0, 0);
    light.castShadow = true;
    light.shadow.bias = -0.001;
    light.shadow.mapSize.width = 2048;
    light.shadow.mapSize.height = 2048;
    light.shadow.camera.near = 0.5;
    light.shadow.camera.far = 500.0;
    light.shadow.camera.left = 100;
    light.shadow.camera.right = -100;
    light.shadow.camera.top = 100;
    light.shadow.camera.bottom = -100;
    this._scene.add(light);

    light = new THREE.AmbientLight(0x101010);
    this._scene.add(light);

    const controls = new OrbitControls(
      this._camera, this._threejs.domElement);
    controls.target.set(0, 20, 0);
    controls.update();

    const loader = new THREE.CubeTextureLoader();
    const textur = loader.load([
        './textures/skybox/posx.jpg',
        './textures/skybox/negx.jpg',
        './textures/skybox/posy.jpg',
        './textures/skybox/negy.jpg',
        './textures/skybox/posz.jpg',
        './textures/skybox/negz.jpg',
    ]);

    this._scene.background = textur;

    const box = new THREE.Mesh(
      new THREE.BoxGeometry(2, 2, 2),
      new THREE.MeshStandardMaterial({
          color: 0xFFFFFF,
      }));
    box.position.set(0, 1, 0);
    box.castShadow = true;
    box.receiveShadow = true;
    this._scene.add(box);

    this._LoadObjects({{ data }})
    this._RAF();
  }

     //create objects from json
    _LoadObjects(data) {
         //draw all objects from source
        for (const [key, value] of Object.entries(data)) {
             //draw color or texture
            if ('texture' in value.material){
                var material = 
                    new THREE[value.material_type]({ map: new THREE.TextureLoader().load(value.material.texture) });
            }else{
                var material = new THREE[value.material_type](value.material);
            }

            const figure = new THREE[value.geometry_type](...Object.values(value.geometry));
            const mesh = new THREE.Mesh(figure, material);
            mesh.name = key;
            mesh.castShadow = value.castShadow
            mesh.receiveShadow = value.receiveShadow
            this._scene.add(mesh);

             //add mesh position
            mesh.position.set(...Object.values(value.position));

             //add mesh rotation
            mesh.rotation.set(...Object.values(value.rotation));
            console.log(value.castShadow)
        }
        console.log(this._scene);
    }

  _OnWindowResize() {
    this._camera.aspect = {{ camera.aspect_ratio }};
    this._camera.updateProjectionMatrix();

    document.getElementById('control').width = 38
    this._threejs.setSize(innerWidth, innerHeight - document.getElementById('control').width);
  }

  _RAF() {
    requestAnimationFrame(() => {
      this._threejs.render(this._scene, this._camera);
      this._RAF();
    });
  }
}


let _APP = null;

window.addEventListener('DOMContentLoaded', () => {
  _APP = new Warehouse();
});
