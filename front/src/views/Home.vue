
<template>
  <div>
    <div
      class="w-screen px-4 py-12 mx-auto sm:px-6 lg:py-16 lg:px-8 lg:items-center lg:justify-between bg-gray-100"
    >
      <h2
        class="text-3xl font-extrabold leading-9 tracking-tight text-gray-900 sm:text-4xl sm:leading-10"
      >
        Interactive mode <br>
        <span class="text-indigo-600 text-2xl sm:text-3xl">Customise your flash code on the fly</span>
      </h2>
      <img 
        src="https://thumbs.gfycat.com/HugeDeliciousArchaeocete-max-1mb.gif" 
        ref="img" alt="qrcode"
        class="rounded-xl mx-auto mt-8" 
        style="max-width: 300px"
      />
      <div class="flex mt-8 lg:flex-shrink-0">
        <div class="flex flex-col w-full">
          <input type="text" class="block rounded-xl border-0 mx-auto" v-model="content">
          <form class="mt-5 flex flex-wrap text-2xl justify-center max-w-screen-sm mx-auto">
            <div class="mx-auto leading-loose mx-5" v-for="m in drawingMethods">
              <label :for="m" class="bg-gray-300 rounded-lg p-1 capitalize" :class="(drawer == m) ? 'font-bold text-3xl' : 'font-normal'">{{ m.replace('_', ' ') }}</label>
              <input :id="m" class="hidden" type="radio" :value="m" v-model="drawer">
            </div>
          </form>
          <a
            download="qrcode.png"
            :href="qrcsrc.length ? qrcsrc[0] : null"
            class="inline-flex items-center justify-center px-5 py-3 font-medium leading-6 text-white transition duration-150 ease-in-out bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-500 focus:outline-none mx-auto mt-8 text-2xl"
            :class="qrcsrc.length ? '' : 'disabled'"
          >
            Download
          </a>
        </div>
      </div>
    </div>
    <AdvancedUsage/>
  </div>
</template>

<script>
  import AdvancedUsage from '../components/AdvancedUsage.vue'
  export default {
    name: 'Home',
    components: { AdvancedUsage },
    data: () => {
      return {
        content: 'test',
        drawingMethods: [
          'classic',
          'vertical_bars',
          'horisontal_bars',
          'rounded',
          'dots'
        ],
        drawer: 'classic',
        qrcsrc: []
      }
    },
    methods: {
      updateimg: function () {
        fetch(`/${this.$data.content}`, 
          {
            method: 'POST',
            body: JSON.stringify({
              drawer: this.$data.drawer
            }),
            headers: {
              "Accept": "image/png",
              "Content-Type": "application/json"
            } 
          }
        )
        .then(r => r.text())
        .then(r => {
          this.$refs.img.src = r
          this.$data.qrcsrc = [ r ]
        })
      }
    },
    watch: {
      content: function (){
        document.title = `${this.$data.content} | QaaS : QRCode as a Service`
        this.updateimg()
      },
      drawer: function (){
        this.updateimg()
      }
    },
    mounted: function () {
      this.updateimg()
    },
    mounted: function () {
      this.$data.content = this.$route.path.substring(1)
    }
  }
</script>
