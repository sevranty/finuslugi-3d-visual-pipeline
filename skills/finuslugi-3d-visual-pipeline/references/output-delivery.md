# Output Delivery

## Finalization order

1. select the highest-scoring approved candidate;
2. complete only approved final integration and upscale;
3. add exact text outside the generative pass;
4. add the approved Finuslugi logo outside the generative pass;
5. export the required format and dimensions;
6. inspect the exported file again;
7. show the final image in the user-facing response.

## Logo rules

From this reference directory:

- white or light background: `../../../assets/finuslugi-base.png`;
- red or dark background: `../../../assets/finuslugi-inverted.png`.

Do not redraw, restyle, distort, or generate the logo.

## Output manifest

Use output manifest version `1.1` and record:

- asset ID, version, and candidate ID;
- Scene Specification version and SHA-256;
- style pack ID and version;
- transformation mode;
- source reference IDs and roles;
- runtime profile ID and adapter ID;
- actual tool and model;
- requested and selected execution modes;
- mandatory capabilities used for route selection;
- every fallback decision, approval, reason, and risk;
- known runtime limitations;
- final dimensions, format, background mode, path, and SHA-256;
- QA score, critical defects, and diagnostic codes;
- visible delivery confirmation and timestamp.

Machine contract: `../assets/schemas/output-manifest.schema.json`.

A requested/selected mode mismatch without a fallback record invalidates the manifest. A completed manifest always includes `deliver` in required capabilities.

## User-facing delivery gate

Before completing the response, verify:

- the generation or edit succeeded;
- the final candidate was selected;
- visual QA passed;
- the final image is attached or rendered in the chat;
- the response is not empty.

A tool success message without a visible final image is not delivery. Emit `DELIVERY_MISSING`, retry only the delivery path, and keep the task incomplete until the image is visible.
