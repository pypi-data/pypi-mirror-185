"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[27425],{89777:(e,t,i)=>{i.d(t,{g:()=>n});const n=e=>e.callWS({type:"cloud/google_assistant/entities"})},27425:(e,t,i)=>{i.a(e,(async e=>{i.r(t);i(44577);var n=i(37500),o=i(33310),s=i(8636),a=i(14516),r=i(47181),l=i(58831),d=i(91741),c=i(45485),h=i(85415),u=i(87744),p=i(65992),f=(i(81545),i(22098),i(83927),i(10983),i(43709),i(83270)),g=i(74186),y=i(89777),m=i(90363),v=i(26765),_=(i(15291),i(60010),i(11654)),k=i(81796),b=i(23182),w=e([p]);function x(){x=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(i){t.forEach((function(t){t.kind===i&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var i=e.prototype;["method","field"].forEach((function(n){t.forEach((function(t){var o=t.placement;if(t.kind===n&&("static"===o||"prototype"===o)){var s="static"===o?e:i;this.defineClassElement(s,t)}}),this)}),this)},defineClassElement:function(e,t){var i=t.descriptor;if("field"===t.kind){var n=t.initializer;i={enumerable:i.enumerable,writable:i.writable,configurable:i.configurable,value:void 0===n?void 0:n.call(e)}}Object.defineProperty(e,t.key,i)},decorateClass:function(e,t){var i=[],n=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!$(e))return i.push(e);var t=this.decorateElement(e,o);i.push(t.element),i.push.apply(i,t.extras),n.push.apply(n,t.finishers)}),this),!t)return{elements:i,finishers:n};var s=this.decorateConstructor(i,t);return n.push.apply(n,s.finishers),s.finishers=n,s},addElementPlacement:function(e,t,i){var n=t[e.placement];if(!i&&-1!==n.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");n.push(e.key)},decorateElement:function(e,t){for(var i=[],n=[],o=e.decorators,s=o.length-1;s>=0;s--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var r=this.fromElementDescriptor(e),l=this.toElementFinisherExtras((0,o[s])(r)||r);e=l.element,this.addElementPlacement(e,t),l.finisher&&n.push(l.finisher);var d=l.extras;if(d){for(var c=0;c<d.length;c++)this.addElementPlacement(d[c],t);i.push.apply(i,d)}}return{element:e,finishers:n,extras:i}},decorateConstructor:function(e,t){for(var i=[],n=t.length-1;n>=0;n--){var o=this.fromClassDescriptor(e),s=this.toClassDescriptor((0,t[n])(o)||o);if(void 0!==s.finisher&&i.push(s.finisher),void 0!==s.elements){e=s.elements;for(var a=0;a<e.length-1;a++)for(var r=a+1;r<e.length;r++)if(e[a].key===e[r].key&&e[a].placement===e[r].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:i}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return D(e,t);var i=Object.prototype.toString.call(e).slice(8,-1);return"Object"===i&&e.constructor&&(i=e.constructor.name),"Map"===i||"Set"===i?Array.from(e):"Arguments"===i||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(i)?D(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var i=S(e.key),n=String(e.placement);if("static"!==n&&"prototype"!==n&&"own"!==n)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+n+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var s={kind:t,key:i,placement:n,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),s.initializer=e.initializer),s},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:L(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var i=L(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:i}},runClassFinishers:function(e,t){for(var i=0;i<t.length;i++){var n=(0,t[i])(e);if(void 0!==n){if("function"!=typeof n)throw new TypeError("Finishers must return a constructor.");e=n}}return e},disallowProperty:function(e,t,i){if(void 0!==e[t])throw new TypeError(i+" can't have a ."+t+" property.")}};return e}function E(e){var t,i=S(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var n={kind:"field"===e.kind?"field":"method",key:i,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(n.decorators=e.decorators),"field"===e.kind&&(n.initializer=e.value),n}function A(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function $(e){return e.decorators&&e.decorators.length}function C(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function L(e,t){var i=e[t];if(void 0!==i&&"function"!=typeof i)throw new TypeError("Expected '"+t+"' to be a function");return i}function S(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var i=e[Symbol.toPrimitive];if(void 0!==i){var n=i.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function D(e,t){(null==t||t>e.length)&&(t=e.length);for(var i=0,n=new Array(t);i<t;i++)n[i]=e[i];return n}function M(){return M="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,i){var n=z(e,t);if(n){var o=Object.getOwnPropertyDescriptor(n,t);return o.get?o.get.call(arguments.length<3?e:i):o.value}},M.apply(this,arguments)}function z(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=P(e)););return e}function P(e){return P=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},P(e)}p=(w.then?await w:w)[0];const V="M10,17L5,12L6.41,10.58L10,14.17L17.59,6.58L19,8M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3Z",O="M22,16A2,2 0 0,1 20,18H8C6.89,18 6,17.1 6,16V4C6,2.89 6.89,2 8,2H20A2,2 0 0,1 22,4V16M16,20V22H4A2,2 0 0,1 2,20V7H4V20H16M13,14L20,7L18.59,5.59L13,11.17L9.91,8.09L8.5,9.5L13,14Z",T="M19,3H16.3H7.7H5A2,2 0 0,0 3,5V7.7V16.4V19A2,2 0 0,0 5,21H7.7H16.4H19A2,2 0 0,0 21,19V16.3V7.7V5A2,2 0 0,0 19,3M15.6,17L12,13.4L8.4,17L7,15.6L10.6,12L7,8.4L8.4,7L12,10.6L15.6,7L17,8.4L13.4,12L17,15.6L15.6,17Z",H="M4 20H18V22H4C2.9 22 2 21.11 2 20V6H4V20M20.22 2H7.78C6.8 2 6 2.8 6 3.78V16.22C6 17.2 6.8 18 7.78 18H20.22C21.2 18 22 17.2 22 16.22V3.78C22 2.8 21.2 2 20.22 2M19 13.6L17.6 15L14 11.4L10.4 15L9 13.6L12.6 10L9 6.4L10.4 5L14 8.6L17.6 5L19 6.4L15.4 10L19 13.6Z";!function(e,t,i,n){var o=x();if(n)for(var s=0;s<n.length;s++)o=n[s](o);var a=t((function(e){o.initializeInstanceElements(e,r.elements)}),i),r=o.decorateClass(function(e){for(var t=[],i=function(e){return"method"===e.kind&&e.key===s.key&&e.placement===s.placement},n=0;n<e.length;n++){var o,s=e[n];if("method"===s.kind&&(o=t.find(i)))if(C(s.descriptor)||C(o.descriptor)){if($(s)||$(o))throw new ReferenceError("Duplicated methods ("+s.key+") can't be decorated.");o.descriptor=s.descriptor}else{if($(s)){if($(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+s.key+").");o.decorators=s.decorators}A(s,o)}else t.push(s)}return t}(a.d.map(E)),e);o.initializeClassElements(a.F,r.elements),o.runClassFinishers(a.F,r.finishers)}([(0,o.Mo)("cloud-google-assistant")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"cloudStatus",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"narrow",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_entities",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_syncing",value:()=>!1},{kind:"field",decorators:[(0,o.SB)()],key:"_entityConfigs",value:()=>({})},{kind:"field",decorators:[(0,o.SB)()],key:"_entityCategories",value:void 0},{kind:"field",key:"_popstateSyncAttached",value:()=>!1},{kind:"field",key:"_popstateReloadStatusAttached",value:()=>!1},{kind:"field",key:"_isInitialExposed",value:void 0},{kind:"field",key:"_getEntityFilterFunc",value:()=>(0,a.Z)((e=>(0,c.h)(e.include_domains,e.include_entities,e.exclude_domains,e.exclude_entities)))},{kind:"method",key:"render",value:function(){if(void 0===this._entities||void 0===this._entityCategories)return n.dy` <hass-loading-screen></hass-loading-screen> `;const e=(0,c.E)(this.cloudStatus.google_entities),t=this._getEntityFilterFunc(this.cloudStatus.google_entities),i=(0,u.Zu)(this.hass),o=this._isInitialExposed||new Set,a=void 0===this._isInitialExposed;let r=0;const l=[],d=[];return this._entities.forEach((c=>{const h=this.hass.states[c.entity_id],u=this._entityConfigs[c.entity_id]||{should_expose:null},p=e?this._configIsExposed(c.entity_id,u,this._entityCategories[c.entity_id]):t(c.entity_id),f=e?this._configIsDomainExposed(c.entity_id,this._entityCategories[c.entity_id]):t(c.entity_id);p&&(r++,a&&o.add(c.entity_id));const g=o.has(c.entity_id)?l:d,y=n.dy`<ha-icon-button
        slot="trigger"
        class=${(0,s.$)({exposed:p,"not-exposed":!p})}
        .disabled=${!e}
        .label=${this.hass.localize("ui.panel.config.cloud.google.expose")}
        .path=${null!==u.should_expose?p?V:T:f?O:H}
      ></ha-icon-button>`;g.push(n.dy`
        <ha-card outlined>
          <div class="card-content">
            <div class="top-line">
              <state-info
                .hass=${this.hass}
                .stateObj=${h}
                secondary-line
                @click=${this._showMoreInfo}
              >
                ${c.entity_id in this.hass.entities?n.dy`<button
                      class="link"
                      .entityId=${c.entity_id}
                      @click=${this._openAliasesSettings}
                    >
                      ${this.hass.localize("ui.panel.config.cloud.google.manage_aliases")}
                    </button>`:""}
              </state-info>
              ${e?n.dy`<ha-button-menu
                    corner="BOTTOM_START"
                    .entityId=${c.entity_id}
                    @action=${this._exposeChanged}
                  >
                    ${y}
                    <mwc-list-item hasMeta>
                      ${this.hass.localize("ui.panel.config.cloud.google.expose_entity")}
                      <ha-svg-icon
                        class="exposed"
                        slot="meta"
                        .path=${V}
                      ></ha-svg-icon>
                    </mwc-list-item>
                    <mwc-list-item hasMeta>
                      ${this.hass.localize("ui.panel.config.cloud.google.dont_expose_entity")}
                      <ha-svg-icon
                        class="not-exposed"
                        slot="meta"
                        .path=${T}
                      ></ha-svg-icon>
                    </mwc-list-item>
                    <mwc-list-item hasMeta>
                      ${this.hass.localize("ui.panel.config.cloud.google.follow_domain")}
                      <ha-svg-icon
                        class=${(0,s.$)({exposed:f,"not-exposed":!f})}
                        slot="meta"
                        .path=${f?O:H}
                      ></ha-svg-icon>
                    </mwc-list-item>
                  </ha-button-menu>`:n.dy`${y}`}
            </div>
            ${c.might_2fa?n.dy`
                  <div>
                    <ha-formfield
                      .label=${this.hass.localize("ui.panel.config.cloud.google.disable_2FA")}
                      .dir=${i}
                    >
                      <ha-switch
                        .entityId=${c.entity_id}
                        .checked=${Boolean(u.disable_2fa)}
                        @change=${this._disable2FAChanged}
                      ></ha-switch>
                    </ha-formfield>
                  </div>
                `:""}
          </div>
        </ha-card>
      `)})),a&&(this._isInitialExposed=o),n.dy`
      <hass-subpage
        .hass=${this.hass}
        .header=${this.hass.localize("ui.panel.config.cloud.google.title")}
        .narrow=${this.narrow}>
        <ha-button-menu corner="BOTTOM_START" slot="toolbar-icon">
          <ha-icon-button
            slot="trigger"
            .label=${this.hass.localize("ui.common.menu")}
            .path=${"M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z"}
          ></ha-icon-button>

          <mwc-list-item
            graphic="icon"
            .disabled=${!e}
            @click=${this._openDomainToggler}
          >
            ${this.hass.localize("ui.panel.config.cloud.google.manage_defaults")}
            <ha-svg-icon
              slot="graphic"
              .path=${"M3,5H9V11H3V5M5,7V9H7V7H5M11,7H21V9H11V7M11,15H21V17H11V15M5,20L1.5,16.5L2.91,15.09L5,17.17L9.59,12.59L11,14L5,20Z"}
            ></ha-svg-icon>
          </mwc-list-item>

          <mwc-list-item
            graphic="icon"
            .disabled=${this._syncing}
            @click=${this._handleSync}
          >
          ${this.hass.localize("ui.panel.config.cloud.google.sync_entities")}
            <ha-svg-icon
              slot="graphic"
              .path=${"M12,18A6,6 0 0,1 6,12C6,11 6.25,10.03 6.7,9.2L5.24,7.74C4.46,8.97 4,10.43 4,12A8,8 0 0,0 12,20V23L16,19L12,15M12,4V1L8,5L12,9V6A6,6 0 0,1 18,12C18,13 17.75,13.97 17.3,14.8L18.76,16.26C19.54,15.03 20,13.57 20,12A8,8 0 0,0 12,4Z"}
            ></ha-svg-icon>
          </mwc-list-item>
        </ha-button-menu>
        ${e?"":n.dy`
                <div class="banner">
                  ${this.hass.localize("ui.panel.config.cloud.google.banner")}
                </div>
              `}
          ${l.length>0?n.dy`
                  <div class="header">
                    <h3>
                      ${this.hass.localize("ui.panel.config.cloud.google.exposed_entities")}
                    </h3>
                    ${this.narrow?r:this.hass.localize("ui.panel.config.cloud.google.exposed","selected",r)}
                  </div>
                  <div class="content">${l}</div>
                `:""}
          ${d.length>0?n.dy`
                  <div class="header second">
                    <h3>
                      ${this.hass.localize("ui.panel.config.cloud.google.not_exposed_entities")}
                    </h3>
                    ${this.narrow?this._entities.length-r:this.hass.localize("ui.panel.config.cloud.google.not_exposed","selected",this._entities.length-r)}
                  </div>
                  <div class="content">${d}</div>
                `:""}
        </div>
      </hass-subpage>
    `}},{kind:"method",key:"firstUpdated",value:function(e){M(P(i.prototype),"firstUpdated",this).call(this,e),this._fetchData()}},{kind:"method",key:"updated",value:function(e){var t;if(M(P(i.prototype),"updated",this).call(this,e),e.has("cloudStatus")&&(this._entityConfigs=this.cloudStatus.prefs.google_entity_configs),e.has("hass")&&(null===(t=e.get("hass"))||void 0===t?void 0:t.entities)!==this.hass.entities){const e={};for(const t of Object.values(this.hass.entities))e[t.entity_id]=t.entity_category;this._entityCategories=e}}},{kind:"method",key:"_openAliasesSettings",value:async function(e){e.stopPropagation();const t=e.target.entityId,i=await(0,g.L3)(this.hass,t);i&&(0,b.l)(this,{entity:i,updateEntry:async e=>{await(0,g.Nv)(this.hass,i.entity_id,e)}})}},{kind:"method",key:"_configIsDomainExposed",value:function(e,t){const i=(0,l.M)(e);return!this.cloudStatus.prefs.google_default_expose||!t&&this.cloudStatus.prefs.google_default_expose.includes(i)}},{kind:"method",key:"_configIsExposed",value:function(e,t,i){var n;return null!==(n=t.should_expose)&&void 0!==n?n:this._configIsDomainExposed(e,i)}},{kind:"method",key:"_fetchData",value:async function(){const e=await(0,y.g)(this.hass);e.sort(((e,t)=>{const i=this.hass.states[e.entity_id],n=this.hass.states[t.entity_id];return(0,h.$)(i?(0,d.C)(i):e.entity_id,n?(0,d.C)(n):t.entity_id,this.hass.locale.language)})),this._entities=e}},{kind:"method",key:"_showMoreInfo",value:function(e){const t=e.currentTarget.stateObj.entity_id;(0,r.B)(this,"hass-more-info",{entityId:t})}},{kind:"method",key:"_exposeChanged",value:async function(e){const t=e.currentTarget.entityId;let i=null;switch(e.detail.index){case 0:i=!0;break;case 1:i=!1;break;case 2:i=null}await this._updateExposed(t,i)}},{kind:"method",key:"_updateExposed",value:async function(e,t){await this._updateConfig(e,{should_expose:t}),this.cloudStatus.google_registered&&this._ensureEntitySync()}},{kind:"method",key:"_disable2FAChanged",value:async function(e){const t=e.currentTarget.entityId,i=e.target.checked;i!==Boolean((this._entityConfigs[t]||{}).disable_2fa)&&await this._updateConfig(t,{disable_2fa:i})}},{kind:"method",key:"_updateConfig",value:async function(e,t){const i=await(0,f.QD)(this.hass,e,t);this._entityConfigs={...this._entityConfigs,[e]:i},this._ensureStatusReload()}},{kind:"method",key:"_openDomainToggler",value:function(){(0,m._)(this,{title:this.hass.localize("ui.panel.config.cloud.google.manage_defaults"),description:this.hass.localize("ui.panel.config.cloud.google.manage_defaults_dialog_description"),domains:this._entities.map((e=>(0,l.M)(e.entity_id))).filter(((e,t,i)=>i.indexOf(e)===t)),exposedDomains:this.cloudStatus.prefs.google_default_expose,toggleDomain:(e,t)=>{this._updateDomainExposed(e,t)},resetDomain:e=>{this._entities.forEach((t=>{(0,l.M)(t.entity_id)===e&&this._updateExposed(t.entity_id,null)}))}})}},{kind:"method",key:"_updateDomainExposed",value:async function(e,t){const i=this.cloudStatus.prefs.google_default_expose||this._entities.map((e=>(0,l.M)(e.entity_id))).filter(((e,t,i)=>i.indexOf(e)===t));t&&i.includes(e)||!t&&!i.includes(e)||(t?i.push(e):i.splice(i.indexOf(e),1),await(0,f.LV)(this.hass,{google_default_expose:i}),(0,r.B)(this,"ha-refresh-cloud-status"))}},{kind:"method",key:"_ensureStatusReload",value:function(){if(this._popstateReloadStatusAttached)return;this._popstateReloadStatusAttached=!0;const e=this.parentElement;window.addEventListener("popstate",(()=>(0,r.B)(e,"ha-refresh-cloud-status")),{once:!0})}},{kind:"method",key:"_handleSync",value:async function(){this._syncing=!0;try{await(0,f.A$)(this.hass)}catch(e){(0,v.Ys)(this,{title:this.hass.localize("ui.panel.config.cloud.google."+(404===e.status_code?"not_configured_title":"sync_failed_title")),text:this.hass.localize("ui.panel.config.cloud.google."+(404===e.status_code?"not_configured_text":"sync_failed_text"))}),(0,r.B)(this,"ha-refresh-cloud-status")}finally{this._syncing=!1}}},{kind:"method",key:"_ensureEntitySync",value:function(){if(this._popstateSyncAttached)return;this._popstateSyncAttached=!0;const e=this.parentElement;window.addEventListener("popstate",(()=>{(0,k.C)(e,{message:this.hass.localize("ui.panel.config.cloud.google.sync_to_google")}),(0,f.A$)(this.hass)}),{once:!0})}},{kind:"get",static:!0,key:"styles",value:function(){return[_.Qx,_.k1,n.iv`
        mwc-list-item > [slot="meta"] {
          margin-left: 4px;
        }
        .banner {
          color: var(--primary-text-color);
          background-color: var(
            --ha-card-background,
            var(--card-background-color, white)
          );
          padding: 16px 8px;
          text-align: center;
        }
        .content {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
          grid-gap: 8px 8px;
          padding: 8px;
        }
        .card-content {
          padding-bottom: 12px;
        }
        state-info {
          cursor: pointer;
        }
        ha-switch {
          padding: 8px 0;
        }
        .top-line {
          display: flex;
          align-items: center;
          justify-content: space-between;
        }
        .header {
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: 0 16px;
          border-bottom: 1px solid var(--divider-color);
          background: var(--app-header-background-color);
        }
        .header.second {
          border-top: 1px solid var(--divider-color);
        }
        .exposed {
          color: var(--success-color);
        }
        .not-exposed {
          color: var(--error-color);
        }
        @media all and (max-width: 450px) {
          ha-card {
            max-width: 100%;
          }
        }
      `]}}]}}),n.oi)}))},23182:(e,t,i)=>{i.d(t,{l:()=>s});var n=i(47181);const o=()=>Promise.all([i.e(85084),i.e(78874),i.e(77576),i.e(68101),i.e(26680)]).then(i.bind(i,15590)),s=(e,t)=>{(0,n.B)(e,"show-dialog",{dialogTag:"dialog-entity-aliases",dialogImport:o,dialogParams:t})}}}]);
//# sourceMappingURL=90227cc8.js.map