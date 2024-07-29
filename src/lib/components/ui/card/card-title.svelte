<script lang="ts">
	import type { HTMLAttributes } from "svelte/elements";
	import type { HeadingLevel } from "./index.js";
	import { cn } from "$lib/utils.js";

	type $$Props = HTMLAttributes<HTMLHeadingElement> & {
		tag?: HeadingLevel;
	};

	let class: $$Props["class"] = undefined;
	export let tag: $$Props["tag"] = "h3";
	export { class as class };
</script>

<svelte:element
	this={tag}
	class={cn("font-semibold leading-none tracking-tight", class)}
	{...$$restProps}
>
	<slot />
</svelte:element>
