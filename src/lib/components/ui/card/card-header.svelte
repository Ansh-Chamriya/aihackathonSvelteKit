<script lang="ts">
	import type { HTMLAttributes } from "svelte/elements";
	import { cn } from "$lib/utils.js";

	type $$Props = HTMLAttributes<HTMLDivElement>;

	let class: $$Props["class"] = undefined;
	export { class as class };
</script>

<div class={cn("flex flex-col space-y-1.5 p-6", class)} {...$$restProps}>
	<slot />
</div>
