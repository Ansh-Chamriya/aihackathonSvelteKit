<script lang="ts">
  import { onMount } from "svelte";
  import SparkleIcon from "$lib/components/SparkleIcon.svelte";
  import GithubIcon from "$lib/components/GithubIcon.svelte";
  import SunIcon from "$lib/components/SunIcon.svelte";
  import MoonIcon from "$lib/components/MoonIcon.svelte";
  import { Button } from "$lib/components/ui/button";
  import { Label } from "$lib/components/ui/label";
  import { Switch } from "$lib/components/ui/switch";
  //   import TickerTape from './TickerTape.svelte';
  //   import AdvancedRealTimeChart from './AdvancedRealTimeChart.svelte';
  import * as Card from "$lib/components/ui/card";
  import { Input } from "$lib/components/ui/input";
  import { Send } from "lucide-svelte";

  export let darkMode = false;
  let prompt = "";

  function handleSwitchChange(event) {
    darkMode = event.detail;
  }
</script>

<div
  class="flex flex-col h-full {darkMode
    ? 'bg-gray-900 text-white'
    : 'bg-gray-100 text-black'}"
>
  <header
    class="flex items-center justify-between p-2 border-b border-gray-700 h-14 {darkMode
      ? ''
      : 'bg-gray-100'}"
  >
    <div class="flex items-center space-x-2">
      <SparkleIcon
        class="w-6 h-6 {darkMode ? 'text-purple-500' : 'text-purple-700'}"
      />
      <span>Stock Saarthi</span>
    </div>
    <div class="flex items-center space-x-4">
      <Button variant="ghost" size="icon" class="rounded-full">
        <GithubIcon class="w-6 h-6" />
      </Button>
      <div class="flex items-center space-x-2">
        <Label class="text-sm flex items-center space-x-2">
          {#if darkMode}
            <SunIcon class="w-5 h-5" />
          {:else}
            <MoonIcon class="w-5 h-5" />
          {/if}
        </Label>
        <Switch
          checked={darkMode}
          on:change={handleSwitchChange}
          class="ring-orange-500 focus:ring-2 rounded-full {darkMode
            ? 'ring-2 ring-orange-500'
            : ''}"
        />
      </div>
    </div>
  </header>
  <!-- <TickerTape copyrightStyles={styles} colorTheme="dark" /> -->
  <main class="flex flex-1 relative">
    <section>
      <!-- <AdvancedRealTimeChart
        container_id="tradingview_1"
        theme="dark"
        width={980}
        symbol="BSE:ITC"
        timezone="Asia/Kolkata"
        height={570}
        interval="D"
        allow_symbol_change={true}
        details={true}
        copyrightStyles={styles}
      /> -->
    </section>
    <section class="w-1/3 p-4 flex-shrink-0 overflow-auto">
      <div class="border-l border-{darkMode ? 'gray-700' : 'gray-300'} h-full">
        <Card
          class="h-[100%] {darkMode ? 'bg-white' : 'bg-[#111827] text-white'}"
        >
          <Card.Header>
            <Card.Title>Chatbot Response</Card.Title>
            <Card.Description class="text-gray-400">
              Responses from the stock market analyst model will appear here.
            </Card.Description>
          </Card.Header>
          <Card.Content class="flex-1 overflow-auto">
            <div class="space-y-4">
              <p>Response 1: Stock XYZ is expected to rise by 5%.</p>
              <p>Response 2: Stock ABC has a stable outlook.</p>
              <p>Response 3: Consider buying stock DEF.</p>
            </div>
          </Card.Content>
        </Card>
      </div>
    </section>
  </main>
  <footer class="p-[0.66rem] border-t border-gray-700">
    <div class="flex items-center space-x-2">
      <form action="">
        <Input
          placeholder="Enter the prompt."
          class="flex-1 rounded-full px-4 py-1 w-64 text-gray-600 {darkMode
            ? ''
            : 'bg-gray-900 text-gray-100'}"
          bind:value={prompt}
        />
        <Button
          variant={darkMode ? "secondary" : "default"}
          class="rounded-full"
        >
          <Send color={darkMode ? "#0d0808" : "#ffffff"} />
        </Button>
      </form>
    </div>
  </footer>
</div>
