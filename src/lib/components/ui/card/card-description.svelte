<script lang="ts">
	import type { HTMLAttributes } from "svelte/elements";
	import { cn } from "$lib/utils.js";

	type $$Props = HTMLAttributes<HTMLParagraphElement>;

	let class: $$Props["class"] = undefined;
	export { class as class };
</script>

<p class={cn("text-muted-foreground text-sm", class)} {...$$restProps}>
	<slot />
</p>
