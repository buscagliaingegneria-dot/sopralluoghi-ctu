---
name: project-website-builder
description: "Turns a project deck PDF, renders, site photos or drawing images into one web page that reads on a phone and can be sent as a link. Uses only the words and numbers in the files or typed in the chat, lists what it found and asks how each part should be shown (full width or grid, side by side or slider, one scroll or one section per screen) before building, keeps PDF drawings sharp when zoomed, and writes the page as one index.html that a drag-and-drop host can put online. Trigger on \"make this a website\", \"project website\", \"send the deck as a link\", \"shareable project page\", \"a page the client can open on their phone\", \"project-website-builder\", or files attached with a request for something a client can open. It does not write project copy, and it does not put anything online by itself."
license: MIT
metadata:
  title: "Project Website Builder"
  summary: "Turn a project PDF or images into one web page you can send as a link"
  discipline: "design-building-types"
  tags: "Design, Document Generation"
---

# Project Website Builder

A deck or a folder of renders becomes one page that scrolls on a phone, opens
the drawings full screen, and goes out as a link.

## Scope and limits — read first

**What this does.** Takes a PDF, images (JPG, PNG), or both, asks how each part
should be shown, and builds one web page the way the user picked. Writes it as
a single file with everything inside, ready to share.

**What this does not do.**

- **It writes no new text.** Every word and number comes from the files or from
  the chat. If there is no project name anywhere, it asks for one.
- It does not correct the files. A wrong area in the PDF is a wrong area on the
  page.
- It does not put the page online. The last section says how.

**What you need.** The files.

## Workflow

### Step 1. Take out what is in the files

- **Photos in a PDF:** the image itself, never a screenshot of the page.
- **Drawing sheets in a PDF:** kept as drawings, not pictures, so they stay
  sharp when zoomed.
- **Images:** as given, resized to about 1,600 px wide.
- **Words:** the PDF's own text and anything typed in the chat. Nothing else.

### Step 2. Let the user lay it out

Do not pick the layout. List what was found, in order, with the ways each one
can be shown, and ask in one message:

> Here is what I found. For each one, pick how to show it, move it, or cut it.
> 1. Cover photo: full width with the project name, or a smaller photo above it?
> 2. The numbers: large on their own, or a short table?
> 3. Model view and render: side by side, or one slider?
> 4. Floor plan: full width, or small and tap to open?
> ...
> And the page as a whole: one long scroll, or one section per screen?
> The PDF's own colours, light, or dark?

The ways to offer, by kind:

| Kind | Ways to show it |
|---|---|
| Photo | Full width · a grid · one at a time, swiped |
| Two images of the same view | Side by side · one slider |
| Drawing | Full width, tap to zoom · small, tap to open |
| Numbers | Large on their own · a short table |

Build only after the answer. If the user says "you choose", take the first way
in each row. Buttons are icons, not words.

### Step 3. Write one file

A folder named for the project, holding one index.html with every image inside
it. The folder is what a drag-and-drop host takes, and the page is named after
the project so a pasted link shows the name.

### Step 4. Check it

- Open it at phone width and check nothing scrolls sideways.
- Find every word on the page in the files or the chat. Anything not found comes
  out.

Then report the folder path, the file size, and how to share it.

## Sharing it

The page is one file, so it can go out three ways:

1. **As a link, through Claude.** If your Claude offers to publish the page,
   take it and copy the link.
2. **As a link, through a free host.** Drag the project folder onto
   app.netlify.com/drop. The link appears straight away; sign in to keep it
   online.
3. **As an attachment.** It opens in a web browser once downloaded, with
   nothing else needed.

**Anyone with the link can open the page.** When it shows a house that is not
built yet or carries a street address, the client agrees before the link goes
out.
