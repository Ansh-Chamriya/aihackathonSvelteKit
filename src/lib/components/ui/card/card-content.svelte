<script lang="ts">
	import type { HTMLAttributes } from "svelte/elements";
	import { cn } from "$lib/utils.js";

	type $$Props = HTMLAttributes<HTMLDivElement>;

	let class: $$Props["class"] = undefined;
	export { class as class };
</script>

<div class={cn("p-6 pt-0", class)} {...$$restProps}>
	<slot />
</div>
