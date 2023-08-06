"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[7916],{25516:(t,e,i)=>{i.d(e,{i:()=>r});const r=t=>e=>({kind:"method",placement:"prototype",key:e.key,descriptor:{set(t){this[`__${String(e.key)}`]=t},get(){return this[`__${String(e.key)}`]},enumerable:!0,configurable:!0},finisher(i){const r=i.prototype.connectedCallback;i.prototype.connectedCallback=function(){if(r.call(this),this[e.key]){const i=this.renderRoot.querySelector(t);if(!i)return;i.scrollTop=this[e.key]}}}})},32594:(t,e,i)=>{i.d(e,{U:()=>r});const r=t=>t.stopPropagation()},93748:(t,e,i)=>{i.d(e,{B$:()=>n,Yc:()=>o,Gd:()=>a,Es:()=>s,SC:()=>c,r4:()=>d,SQ:()=>u,sq:()=>p,Ip:()=>h,HF:()=>f,Pl:()=>m,Xm:()=>y,J8:()=>g});var r=i(83849);const n="single",o=10,a=t=>{if("condition"in t&&Array.isArray(t.condition))return{condition:"and",conditions:t.condition};for(const e of["and","or","not"])if(e in t)return{condition:e,conditions:t[e]};return t},s=(t,e)=>{t.callService("automation","trigger",{entity_id:e,skip_condition:!0})},c=(t,e)=>t.callApi("DELETE",`config/automation/config/${e}`);let l;const d=(t,e)=>t.callApi("GET",`config/automation/config/${e}`),u=(t,e)=>t.callWS({type:"automation/config",entity_id:e}),p=(t,e,i)=>t.callApi("POST",`config/automation/config/${e}`,i),h=t=>{l=t,(0,r.c)("/config/automation/edit/new")},f=t=>{h({...t,id:void 0,alias:void 0})},m=()=>{const t=l;return l=void 0,t},y=(t,e,i,r)=>t.connection.subscribeMessage(e,{type:"subscribe_trigger",trigger:i,variables:r}),g=(t,e,i)=>t.callWS({type:"test_condition",condition:e,variables:i})},26765:(t,e,i)=>{i.d(e,{Ys:()=>a,g7:()=>s,D9:()=>c});var r=i(47181);const n=()=>Promise.all([i.e(85084),i.e(1281)]).then(i.bind(i,1281)),o=(t,e,i)=>new Promise((o=>{const a=e.cancel,s=e.confirm;(0,r.B)(t,"show-dialog",{dialogTag:"dialog-box",dialogImport:n,dialogParams:{...e,...i,cancel:()=>{o(!(null==i||!i.prompt)&&null),a&&a()},confirm:t=>{o(null==i||!i.prompt||t),s&&s(t)}}})})),a=(t,e)=>o(t,e),s=(t,e)=>o(t,e,{confirmation:!0}),c=(t,e)=>o(t,e,{prompt:!0})},83114:(t,e,i)=>{i.a(t,(async t=>{i.r(e);i(22098),i(48932),i(58856),i(54444);var r=i(37500),n=i(33310),o=(i(42173),i(47181)),a=i(83849),s=(i(47150),i(36125),i(52039),i(67556),i(93748)),c=i(11654),l=i(22311),d=i(44583),u=i(14516),p=(i(67065),t([d]));function h(){h=function(){return t};var t={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(t,e){["method","field"].forEach((function(i){e.forEach((function(e){e.kind===i&&"own"===e.placement&&this.defineClassElement(t,e)}),this)}),this)},initializeClassElements:function(t,e){var i=t.prototype;["method","field"].forEach((function(r){e.forEach((function(e){var n=e.placement;if(e.kind===r&&("static"===n||"prototype"===n)){var o="static"===n?t:i;this.defineClassElement(o,e)}}),this)}),this)},defineClassElement:function(t,e){var i=e.descriptor;if("field"===e.kind){var r=e.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===r?void 0:r.call(t)}}Object.defineProperty(t,e.key,i)},decorateClass:function(t,e){var i=[],r=[],n={static:[],prototype:[],own:[]};if(t.forEach((function(t){this.addElementPlacement(t,n)}),this),t.forEach((function(t){if(!y(t))return i.push(t);var e=this.decorateElement(t,n);i.push(e.element),i.push.apply(i,e.extras),r.push.apply(r,e.finishers)}),this),!e)return{elements:i,finishers:r};var o=this.decorateConstructor(i,e);return r.push.apply(r,o.finishers),o.finishers=r,o},addElementPlacement:function(t,e,i){var r=e[t.placement];if(!i&&-1!==r.indexOf(t.key))throw new TypeError("Duplicated element ("+t.key+")");r.push(t.key)},decorateElement:function(t,e){for(var i=[],r=[],n=t.decorators,o=n.length-1;o>=0;o--){var a=e[t.placement];a.splice(a.indexOf(t.key),1);var s=this.fromElementDescriptor(t),c=this.toElementFinisherExtras((0,n[o])(s)||s);t=c.element,this.addElementPlacement(t,e),c.finisher&&r.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],e);i.push.apply(i,l)}}return{element:t,finishers:r,extras:i}},decorateConstructor:function(t,e){for(var i=[],r=e.length-1;r>=0;r--){var n=this.fromClassDescriptor(t),o=this.toClassDescriptor((0,e[r])(n)||n);if(void 0!==o.finisher&&i.push(o.finisher),void 0!==o.elements){t=o.elements;for(var a=0;a<t.length-1;a++)for(var s=a+1;s<t.length;s++)if(t[a].key===t[s].key&&t[a].placement===t[s].placement)throw new TypeError("Duplicated element ("+t[a].key+")")}}return{elements:t,finishers:i}},fromElementDescriptor:function(t){var e={kind:t.kind,key:t.key,placement:t.placement,descriptor:t.descriptor};return Object.defineProperty(e,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===t.kind&&(e.initializer=t.initializer),e},toElementDescriptors:function(t){var e;if(void 0!==t)return(e=t,function(t){if(Array.isArray(t))return t}(e)||function(t){if("undefined"!=typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)}(e)||function(t,e){if(t){if("string"==typeof t)return k(t,e);var i=Object.prototype.toString.call(t).slice(8,-1);return"Object"===i&&t.constructor&&(i=t.constructor.name),"Map"===i||"Set"===i?Array.from(t):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?k(t,e):void 0}}(e)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(t){var e=this.toElementDescriptor(t);return this.disallowProperty(t,"finisher","An element descriptor"),this.disallowProperty(t,"extras","An element descriptor"),e}),this)},toElementDescriptor:function(t){var e=String(t.kind);if("method"!==e&&"field"!==e)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+e+'"');var i=b(t.key),r=String(t.placement);if("static"!==r&&"prototype"!==r&&"own"!==r)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+r+'"');var n=t.descriptor;this.disallowProperty(t,"elements","An element descriptor");var o={kind:e,key:i,placement:r,descriptor:Object.assign({},n)};return"field"!==e?this.disallowProperty(t,"initializer","A method descriptor"):(this.disallowProperty(n,"get","The property descriptor of a field descriptor"),this.disallowProperty(n,"set","The property descriptor of a field descriptor"),this.disallowProperty(n,"value","The property descriptor of a field descriptor"),o.initializer=t.initializer),o},toElementFinisherExtras:function(t){return{element:this.toElementDescriptor(t),finisher:v(t,"finisher"),extras:this.toElementDescriptors(t.extras)}},fromClassDescriptor:function(t){var e={kind:"class",elements:t.map(this.fromElementDescriptor,this)};return Object.defineProperty(e,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),e},toClassDescriptor:function(t){var e=String(t.kind);if("class"!==e)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+e+'"');this.disallowProperty(t,"key","A class descriptor"),this.disallowProperty(t,"placement","A class descriptor"),this.disallowProperty(t,"descriptor","A class descriptor"),this.disallowProperty(t,"initializer","A class descriptor"),this.disallowProperty(t,"extras","A class descriptor");var i=v(t,"finisher");return{elements:this.toElementDescriptors(t.elements),finisher:i}},runClassFinishers:function(t,e){for(var i=0;i<e.length;i++){var r=(0,e[i])(t);if(void 0!==r){if("function"!=typeof r)throw new TypeError("Finishers must return a constructor.");t=r}}return t},disallowProperty:function(t,e,i){if(void 0!==t[e])throw new TypeError(i+" can't have a ."+e+" property.")}};return t}function f(t){var e,i=b(t.key);"method"===t.kind?e={value:t.value,writable:!0,configurable:!0,enumerable:!1}:"get"===t.kind?e={get:t.value,configurable:!0,enumerable:!1}:"set"===t.kind?e={set:t.value,configurable:!0,enumerable:!1}:"field"===t.kind&&(e={configurable:!0,writable:!0,enumerable:!0});var r={kind:"field"===t.kind?"field":"method",key:i,placement:t.static?"static":"field"===t.kind?"own":"prototype",descriptor:e};return t.decorators&&(r.decorators=t.decorators),"field"===t.kind&&(r.initializer=t.value),r}function m(t,e){void 0!==t.descriptor.get?e.descriptor.get=t.descriptor.get:e.descriptor.set=t.descriptor.set}function y(t){return t.decorators&&t.decorators.length}function g(t){return void 0!==t&&!(void 0===t.value&&void 0===t.writable)}function v(t,e){var i=t[e];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+e+"' to be a function");return i}function b(t){var e=function(t,e){if("object"!=typeof t||null===t)return t;var i=t[Symbol.toPrimitive];if(void 0!==i){var r=i.call(t,e||"default");if("object"!=typeof r)return r;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===e?String:Number)(t)}(t,"string");return"symbol"==typeof e?e:String(e)}function k(t,e){(null==e||e>t.length)&&(e=t.length);for(var i=0,r=new Array(e);i<e;i++)r[i]=t[i];return r}function w(){return w="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(t,e,i){var r=E(t,e);if(r){var n=Object.getOwnPropertyDescriptor(r,e);return n.get?n.get.call(arguments.length<3?t:i):n.value}},w.apply(this,arguments)}function E(t,e){for(;!Object.prototype.hasOwnProperty.call(t,e)&&null!==(t=_(t)););return t}function _(t){return _=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(t){return t.__proto__||Object.getPrototypeOf(t)},_(t)}d=(p.then?await p:p)[0];!function(t,e,i,r){var n=h();if(r)for(var o=0;o<r.length;o++)n=r[o](n);var a=e((function(t){n.initializeInstanceElements(t,s.elements)}),i),s=n.decorateClass(function(t){for(var e=[],i=function(t){return"method"===t.kind&&t.key===o.key&&t.placement===o.placement},r=0;r<t.length;r++){var n,o=t[r];if("method"===o.kind&&(n=e.find(i)))if(g(o.descriptor)||g(n.descriptor)){if(y(o)||y(n))throw new ReferenceError("Duplicated methods ("+o.key+") can't be decorated.");n.descriptor=o.descriptor}else{if(y(o)){if(y(n))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+o.key+").");n.decorators=o.decorators}m(o,n)}else e.push(o)}return e}(a.d.map(f)),t);n.initializeClassElements(a.F,s.elements),n.runClassFinishers(a.F,s.finishers)}([(0,n.Mo)("ha-panel-aisttsauto")],(function(t,e){class i extends e{constructor(...e){super(...e),t(this)}}return{F:i,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"isWide",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"narrow",value:void 0},{kind:"field",key:"_columns",value(){return(0,u.Z)(((t,e)=>{const i={toggle:{title:r.dy`&nbsp;&nbsp;&nbsp;&nbsp;<ha-svg-icon
              path=${"M1,11H3.17C3.58,9.83 4.69,9 6,9C6.65,9 7.25,9.21 7.74,9.56L14.44,4.87L15.58,6.5L8.89,11.2C8.96,11.45 9,11.72 9,12A3,3 0 0,1 6,15C4.69,15 3.58,14.17 3.17,13H1V11M23,11V13H20.83C20.42,14.17 19.31,15 18,15A3,3 0 0,1 15,12A3,3 0 0,1 18,9C19.31,9 20.42,9.83 20.83,11H23M6,11A1,1 0 0,0 5,12A1,1 0 0,0 6,13A1,1 0 0,0 7,12A1,1 0 0,0 6,11M18,11A1,1 0 0,0 17,12A1,1 0 0,0 18,13A1,1 0 0,0 19,12A1,1 0 0,0 18,11Z"}
            ></ha-svg-icon>`,type:"icon",template:(t,e)=>r.dy`
              <ha-checkbox
                .key=${e.id}
                .hass=${this.hass}
                @change=${this._handleRowCheckboxClick}
                .checked=${"on"===e.entity.state}
              >
              </ha-checkbox>
            `},name:{title:"Nazwa",sortable:!0,filterable:!0,direction:"asc",grows:!0}};return t||(i.last_triggered={sortable:!0,width:"20%",title:this.hass.localize("ui.card.automation.last_triggered"),template:t=>r.dy`
            ${t?(0,d.o0)(new Date(t),this.hass.locale):this.hass.localize("ui.components.relative_time.never")}
          `},i.trigger={title:r.dy`
            <mwc-button style="visibility: hidden">
              ${this.hass.localize("ui.card.automation.trigger")}
            </mwc-button>
          `,width:"20%",template:(t,e)=>r.dy`
            <mwc-button
              .automation=${e.entity}
              @click=${t=>this._runActions(t)}
            >
              URUCHOM
            </mwc-button>
          `}),this.hass.user.is_admin&&(i.info={title:"",type:"icon-button",template:(t,e)=>r.dy`
            <mwc-icon-button
              .automation=${e.entity}
              @click=${this._showInfo}
              label="Info"
            >
              <ha-svg-icon .path=${"M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z"}></ha-svg-icon>
            </mwc-icon-button>
          `},i.trace={title:"",type:"icon-button",template:(t,e)=>r.dy`
            <a
              href="/config/automation/trace/${e.entity.attributes.id}"
            >
              <mwc-icon-button label="Ślad">
                <ha-svg-icon .path=${"M13.5,8H12V13L16.28,15.54L17,14.33L13.5,12.25V8M13,3A9,9 0 0,0 4,12H1L4.96,16.03L9,12H6A7,7 0 0,1 13,5A7,7 0 0,1 20,12A7,7 0 0,1 13,19C11.07,19 9.32,18.21 8.06,16.94L6.64,18.36C8.27,20 10.5,21 13,21A9,9 0 0,0 22,12A9,9 0 0,0 13,3"}></ha-svg-icon>
              </mwc-icon-button>
            </a>
          `},i.edit={title:"",type:"icon-button",template:(t,e)=>r.dy`
            <a
              href="/config/automation/edit/${e.entity.attributes.id}"
            >
              <mwc-icon-button label="Edit">
                <ha-svg-icon path=${"M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z"}></ha-svg-icon>
              </mwc-icon-button>
            </a>
          `}),i}))}},{kind:"method",key:"firstUpdated",value:function(t){w(_(i.prototype),"firstUpdated",this).call(this,t)}},{kind:"method",key:"_get_automations",value:function(t){const e=[];return Object.values(this.hass.states).forEach((t=>{"automation"!==(0,l.N)(t)||t.entity_id.startsWith("automation.ais_")||e.push({id:t.entity_id,name:t.attributes.friendly_name,last_triggered:t.attributes.last_triggered,entity:t})})),e}},{kind:"method",key:"render",value:function(){return r.dy`
      <ha-app-layout>
        <app-header slot="header" fixed>
          <app-toolbar>
            <ha-menu-button
              .hass=${this.hass}
              .narrow=${this.narrow}
            ></ha-menu-button>
            <div main-title>TTS Automatyczny</div>
            ${this.hass.user.is_admin?r.dy`<ha-icon-button
                  label="Dodaj"
                  icon="hass:plus"
                  @click=${this._createNew}
                ></ha-icon-button>`:r.dy``}
          </app-toolbar>
        </app-header>
        <ha-card class="content">
          <ha-data-table
            .columns=${this._columns(this.narrow,this.hass.locale)}
            .data=${this._get_automations(this.hass.states)}
            auto-height
            searchLabel="Szukaj"
            noDataText="Brak danych"
          ></ha-data-table>
        </ha-card>
      </ha-app-layout>
    `}},{kind:"method",key:"_showInfo",value:function(t){t.stopPropagation();const e=t.currentTarget.automation.entity_id;(0,o.B)(this,"hass-more-info",{entityId:e})}},{kind:"method",key:"_runActions",value:function(t){const e=t.currentTarget.automation.entity_id;(0,s.Es)(this.hass,e)}},{kind:"method",key:"_createNew",value:function(){(0,a.c)("/config/automation/edit/new")}},{kind:"method",key:"_handleRowCheckboxClick",value:function(t){const e=t.currentTarget.key,i=t.currentTarget.hass;let r="off";t.currentTarget.checked&&(r="on"),i.callService("ais_tts","change_auto_mode",{entity_id:e,change_to:r})}},{kind:"get",static:!0,key:"styles",value:function(){return[c.Qx,r.iv`
        ha-card.content {
          padding: 16px;
        }

        .has-header {
          padding-top: 0;
        }

        .checked span {
          color: var(--primary-color);
        }
        .content {
          padding-bottom: 32px;
          max-width: 94%;
          margin: 0 auto;
        }
      `]}}]}}),r.oi)}))}}]);
//# sourceMappingURL=5a9c57b2.js.map