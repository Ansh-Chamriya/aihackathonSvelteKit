<script lang="ts">
  export let data;
  // @ts-ignore
  import TradingViewWidget from "svelte-tradingview-widget";
  import { onMount } from "svelte";
  import SparkleIcon from "$lib/components/SparkleIcon.svelte";
  import GithubIcon from "$lib/components/GithubIcon.svelte";
  import SunIcon from "$lib/components/SunIcon.svelte";
  import MoonIcon from "$lib/components/MoonIcon.svelte";
  import { Button } from "$lib/components/ui/button";
  import { Label } from "$lib/components/ui/label";
  import { Switch } from "$lib/components/ui/switch";

  import * as Card from "$lib/components/ui/card";
  import { Input } from "$lib/components/ui/input";
  import { Send } from "lucide-svelte";
  import TickerTape from "$lib/components/TickerTape.svelte";
  import Chatview from "$lib/chatview.svelte";
  import Chat from "$lib/chat.svelte";

  export let darkMode = true;
  let prompt = "";

  function handleSwitchChange(event) {
    darkMode = event.detail;
  }
  // onMount(async () => {
  //   const data = await fetch("http://127.0.0.1:8000/predict", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     body: JSON.stringify({
  //       description: "give me top 5 stocks. ",
  //     }),
  //   });
  //   const response = await data.json();
  //   console.log(response);
  // });
  let options = {
    symbol: "BSE:ITC",
    interval: "D",
    allow_symbol_change: true,
    details: true,
    timezone: "Asia/Kolkata",
    theme: "dark",
    autosize: true,
  };
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
      <SparkleIcon />
      <span>Stock Saarthi</span>
    </div>
    <div class="flex items-center space-x-4">
      <Button variant="ghost" size="icon" class="rounded-full">
        <GithubIcon />
      </Button>
      <div class="flex items-center space-x-2">
        <Label class="text-sm flex items-center space-x-2">
          {#if darkMode}
            <SunIcon />
          {:else}
            <MoonIcon />
          {/if}
        </Label>
        <Switch
          bind:checked={darkMode}
          class="ring-orange-500 focus:ring-2 rounded-full {darkMode
            ? 'ring-2 ring-orange-500'
            : ''}"
        />
      </div>
    </div>
  </header>
  <TickerTape />

  <main class="flex flex-1 relative">
    <section class="h-[542px] w-[980px]">
      <TradingViewWidget {options} />
    </section>
    <section class="w-1/3 p-4 flex-shrink-0 overflow-auto">
      <div class="border-l border-{darkMode ? 'gray-700' : 'gray-300'} h-full">
        <Card.Root
          class="h-[100%] {darkMode ? 'bg-white' : 'bg-[#111827] text-white'}"
        >
          <Card.Header>
            <Card.Title>Chatbot Response</Card.Title>
            <Card.Description class="text-gray-400">
              Responses from the stock market analyst model will appear here.
            </Card.Description>
          </Card.Header>
          <Card.Content class="flex flex-col justify-between">
            <div class="space-y-4 max-h-80 min-h-80 overflow-y-auto">
              <Chatview></Chatview>
            </div>
            <Chat></Chat>
          </Card.Content>
        </Card.Root>
      </div>
    </section>
  </main>
  <!-- <footer class="p-[0.66rem] border-t border-gray-700">
    <form method="post">
      <div class="flex items-center space-x-2">
        <Input
          name="prompt"
          placeholder="Enter the prompt."
          class="flex-1 rounded-full px-4 py-1 w-64 text-gray-600 {darkMode
            ? 'bg-white'
            : 'bg-gray-900 text-gray-100'}"
          bind:value={prompt}
        />
        <Button
          type="submit"
          variant={darkMode ? "secondary" : "default"}
          class="rounded-full"
        >
          <Send color={darkMode ? "#0d0808" : "#ffffff"} />
        </Button>
      </div>
    </form>
  </footer> -->
</div>
