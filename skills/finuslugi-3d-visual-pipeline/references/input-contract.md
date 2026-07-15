# Input Contract

## Required input

At least one of the following must be present:

- a usable visual reference;
- an existing image that the user wants edited;
- an approved Scene Specification with sufficient visual constraints.

## Required decisions

Before generation, resolve:

- communication message;
- product advantage or narrative purpose;
- primary transformation mode;
- main object;
- supporting elements and exact count when count matters;
- target channel;
- aspect ratio or final dimensions;
- selected style pack and version;
- elements that must be preserved;
- elements that may change;
- forbidden additions.

## Input validation

Reject or clarify when:

- the referenced image is absent from the conversation or project;
- the user refers only to an opaque identifier that cannot be resolved;
- multiple references have conflicting roles;
- exact identity preservation is requested without an adequate identity source;
- required text must be exact but no separate text-production step is allowed;
- the output channel requires dimensions that have not been specified or safely inferred.

## Default assumptions

When the user does not specify otherwise:

- preserve the main subject and communication meaning;
- use composition as guidance rather than a pixel-exact lock;
- create a new image rather than a copy;
- do not include logos or exact text in the generative pass;
- use a single approved style pack;
- keep supporting elements minimal.
