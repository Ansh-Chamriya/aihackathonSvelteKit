<script lang="ts">
  import { liveQuery } from "dexie";
  import { db } from "./db";
  import { marked } from "marked";

  const livechats = liveQuery(() => db.chats.toArray());
  function formatResponse(response: string) {
    const answer = marked(response);
    console.log("answer", answer);

    return answer;
  }
</script>

{#if $livechats}
  <div class="m-3 flex flex-col gap-4">
    {#each $livechats.sort((a, b) => new Date(a.cretaedAt).getTime() - new Date(b.cretaedAt).getTime()) || [] as chat}
      {@const formattedResponse = formatResponse(chat.response)}
      <div class="flex justify-end">
        <p class="items-end px-3 py-2 bg-gray-200">
          {chat.prompt}
        </p>
      </div>
      <div class="flex justify-start">
        <p class="items-end text-pretty px-3 py-2 bg-gray-200">
          {@html formattedResponse}
        </p>
      </div>
    {/each}
  </div>
{/if}

<style>
  p {
    border-radius: 10px;
    background-color: #f3f4f6;
    width: fit-content;
  }
</style>
