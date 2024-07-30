<script lang="ts">
	import { Send } from "lucide-svelte";
	import Button from "./components/ui/button/button.svelte";
	import Input from "./components/ui/input/input.svelte";
	import { enhance } from "$app/forms";
	import { db } from "./db";
	import toast from "svelte-french-toast";

	let prompt = "";
	let iswaiting = false;
	async function getRes() {
		iswaiting = true;
		const req = await fetch("/predict", {
			method: "POST",
			body: JSON.stringify({ prompt }),
			headers: {
				"Content-Type": "application/json",
			},
		});

		if (req.status === 201) {
			const { response } = await req.json();
			db.transaction("rw", db.chats, async () => {
				await db.chats.add({
					prompt: prompt,
					response: response,
					cretaedAt: new Date(),
				});
			})
				.then(() => {
					iswaiting = false;
					prompt = "";
				})
				.catch((e) => {
					toast.error("Try again");
					console.error(e);
				});
		}
	}
</script>

<div>
	<form on:submit={getRes}>
		<div class="flex gap-3">
			<Input
				type="text"
				placeholder="Type a message..."
				bind:value={prompt}
			/>
			<Button type="submit">
				{#if !iswaiting}
					<Send></Send>
				{:else}
					<div
						class="size-4 animate-spin rounded-full border-b-2 border-t-2 border-white"
					></div>
				{/if}
			</Button>
		</div>
	</form>
</div>
