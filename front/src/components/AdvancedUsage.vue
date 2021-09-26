<template>
  <section
    class="max-w-screen-xl px-4 py-12 mx-auto sm:px-6 lg:py-16 lg:px-8 lg:items-center lg:justify-between"
  >
    <h2
      class="text-3xl font-extrabold leading-9 tracking-tight text-gray-900 sm:text-4xl sm:leading-10"
    >
      Advanced Usages
      <br />
      <span class="text-indigo-600 text-2xl sm:text-3xl">For real h4xx0rs</span>
    </h2>

    <article 
      class="mt-10 text-lg"
      v-for="c in commands"
    >
      {{ c.comment }}
      <div 
        class="mt-2 font-mono p-5 rounded-lg bg-gray-200">
        <p class="border-b border-gray-500 pb-5 mb-5">
          {{ c.command }}
        </p>
        <pre class="leading-none">{{ c.result }}</pre>
      </div>
    </article>
  </section>
</template>

<script>
  export default {
    name: 'AdvancedUsage',
    data: () => {
      return {
        commands: [
          {
            comment: 'Generate easily QrCodes from your terminal',
            command: 'curl qrcode.benaben.space/test',
            result: `Here is your qrcode for \`test\` :                              
                             
    █▀▀▀▀▀█ ▄ █ ▄ █▀▀▀▀▀█    
    █ ███ █  ▄▄▀  █ ███ █    
    █ ▀▀▀ █ ▀█ █▀ █ ▀▀▀ █    
    ▀▀▀▀▀▀▀ ▀▄█ ▀ ▀▀▀▀▀▀▀    
    ▀ █▄█▄▀▄  █▄▀▄ ▄▀  █▄    
    ▀ ▀▄▄▄▀▀████▄█▀█▄▀▀█▀    
    ▀ ▀ ▀ ▀ ▄▀▀▀ ▀█▀ █ ▀█    
    █▀▀▀▀▀█  ▀▄ ▀ ▄ ▀▀ █▀    
    █ ███ █ ▀▀█▄▀▄▀▄▀▀ █▀    
    █ ▀▀▀ █ ▀▀██▄█▀█▄▄▀▄▀    
    ▀▀▀▀▀▀▀ ▀▀▀▀ ▀▀▀  ▀▀▀    
                             
                             
`
          }
        ]
      }
    }
  }
</script>