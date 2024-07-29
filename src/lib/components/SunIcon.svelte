<script>
  export let width = "24";
  export let height = "24";
  export let fill = "none";
  export let stroke = "currentColor";
  export let strokeWidth = "2";
  export let strokeLinecap = "round";
  export let strokeLinejoin = "round";
</script>

<svg
  xmlns="http://www.w3.org/2000/svg"
  {width}
  {height}
  viewBox="0 0 24 24"
  {fill}
  {stroke}
  {strokeWidth}
  {strokeLinecap}
  {strokeLinejoin}
>
  <circle cx="12" cy="12" r="4" />
  <path d="M12 2v2" />
  <path d="M12 20v2" />
  <path d="m4.93 4.93 1.41 1.41" />
  <path d="m17.66 17.66 1.41 1.41" />
  <path d="M2 12h2" />
  <path d="M20 12h2" />
  <path d="m6.34 17.66-1.41 1.41" />
  <path d="m19.07 4.93-1.41 1.41" />
</svg>
