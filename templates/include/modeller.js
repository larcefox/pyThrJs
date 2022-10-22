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
    console.log(document.getElementById('control'))
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



    const controls = new OrbitControls(
      this._camera, this._threejs.domElement);
    controls.target.set(0, 20, 0);
    controls.update();

    const loader = new THREE.CubeTextureLoader();
    const textur = loader.load([
        '{{ url_for('static', filename='textures/skybox/posx.jpg') }}',
        '{{ url_for('static', filename='textures/skybox/negx.jpg') }}',
        '{{ url_for('static', filename='textures/skybox/posy.jpg') }}',
        '{{ url_for('static', filename='textures/skybox/negy.jpg') }}',
        '{{ url_for('static', filename='textures/skybox/posz.jpg') }}',
        '{{ url_for('static', filename='textures/skybox/negz.jpg') }}'
    ]);

    this._scene.background = textur;

    //const box = new THREE.Mesh(
      //new THREE.BoxGeometry(2, 2, 2),
      //new THREE.MeshStandardMaterial({
          //color: 0xFFFFFF,
      //}));
    //box.position.set(0, 1, 0);
    //box.castShadow = true;
    //box.receiveShadow = true;
    //this._scene.add(box);

    this._LoadLight( {{ light }} )
    this._LoadEntity({{ entity }})
    this._RAF();
  }

     //create light from json
    _LoadLight(data) {
         //draw all shapes from source
        for (const [key, value] of Object.entries(data)) {
            console.log(value)
            const light = new THREE[value.light_type](
                value.color, 
                value.intencity
            ); 
            light.name = key;

            if (value.light_type == 'DirectionalLight') {
                light.position.set(...Object.values(value.position));
                light.target.position.set(...Object.values(value.target_position));
                light.castShadow = value.castShadow;
                

                light.shadow.bias = light.shadow.bias;
                light.shadow.mapSize = light.shadow.mapSize;
                light.shadow.bias = value.shadow.bias;
                light.shadow.mapSize.width = value.shadow.mapSize.width;
                light.shadow.mapSize.height = value.shadow.mapSize.height;
                light.shadow.camera.near = value.shadow.camera.near;
                light.shadow.camera.far = value.shadow.camera.far;
                light.shadow.camera.left = value.shadow.camera.left;
                light.shadow.camera.right = value.shadow.camera.right;
                light.shadow.camera.top = value.shadow.camera.top;
                light.shadow.camera.bottom = value.shadow.camera.bottom;

                this._scene.add(light);
            }else if (value.light_type == 'AmbientLight'){
                this._scene.add(light);
            }
        }
    }
     //create shapes from json
    _LoadEntity(data) {
         //draw all shapes from source
        for (const [key, value] of Object.entries(data)) {
             //draw color or texture
            let material;
            if ('texture' in value.material){
                material = 
                    new THREE[value.material_type]({ map: new THREE.TextureLoader().load('{{ url_for('static', filename='textures/blueprint.jpg') }}') });
            }else{
                material = new THREE[value.material_type](value.material);
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
