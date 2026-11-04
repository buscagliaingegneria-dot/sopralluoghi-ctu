---
title: Explain COI
summary: Explain a certificate of insurance and what it does not prove
discipline: practice-contracts
tags: ["Reference"]
description: "Reads a certificate of insurance against the coverage a contract requires and explains, in plain English, what each line means and what the certificate does not establish: that it is evidence of a policy rather than the policy, that additional insured status depends on an endorsement the certificate only claims, and that the wording on the face of it is expressly not a modification of coverage. Checks limits, dates, named parties and the gaps that matter to a design professional. Carries no coverage requirements and no policy language; the requirement comes from the contract and the coverage from the policy. It is not insurance advice — the broker reads the policy and the insurer confirms coverage. For advice on what to carry use the `insurance-advisor` skill."
argument-hint: <certificate> [contract-requirement]
---

# Explain COI

A certificate of insurance is a one-page summary produced by a broker, and it
says on its own face that it confers no rights and modifies no coverage. It is
routinely filed as though it proved the coverage exists in the form the contract
requires. It does not.

## Scope and limits — read first

**What this does.** Explains each part of the certificate in plain English,
compares what it shows against what the contract requires, and separates what
the certificate establishes from what it merely asserts.

**What this does not do.**

- **It is not insurance advice.** A broker reads the policy; the insurer
  confirms coverage. This explains a document so the right question can be
  asked.
- It carries **no coverage requirements.** What the contract requires comes from
  the contract, quoted.
- It carries **no policy language.** Exclusions, endorsements and the actual
  scope of cover live in the policy, which a certificate is not.
- It does not advise what to carry. `insurance-advisor` does.
- It does not confirm anything. Where confirmation is needed, the answer is
  always a request to the broker or the insurer.

**What you need before starting.** The certificate. The contract's insurance
requirements, quoted. Who is supposed to be an additional insured and on what
basis.

## Inputs the command needs

1. **The certificate**, complete, including the description of operations box.
2. **The contract's insurance article**, quoted.
3. **The parties** who have to be named, and on what basis.
4. **The project**, so the description box can be checked against it.

## Workflow

### Step 1 — Say what the certificate is

Every run starts here, because it frames the rest:

A certificate is issued by a broker as evidence that policies were in force on
the date issued. It confers no rights, amends nothing, and does not extend
coverage. The policies govern. If the certificate and the policy disagree, the
policy wins.

### Step 2 — Read each line and explain it

Walk the certificate and explain what each coverage line is for, in plain
English:

- **General liability.** Bodily injury and property damage arising from
  operations. Note whether it is occurrence or claims-made, and what each means
  for a claim reported later.
- **Automobile liability.** Whose vehicles: owned, hired, non-owned.
- **Umbrella or excess.** What it sits over, and whether it follows form.
- **Workers compensation and employers liability.** Statutory, and what the
  waiver of subrogation line means.
- **Professional liability.** Almost always claims-made, which means the policy
  in force when the claim is made responds, not the one in force when the work
  was done. Explain what that implies about tail coverage after the project
  ends.

### Step 3 — Compare against the contract, line by line

| Coverage required | Contract says | Certificate shows | Meets it? |
|---|---|---|---|

Check limits per occurrence and aggregate separately. **An aggregate shared
across every project the insured has is not a project limit**, and the contract
may require a per-project aggregate. Say whether the certificate shows one.

### Step 4 — Work the four things a certificate does not establish

This is the part that matters, and each gets stated explicitly:

- **Additional insured status.** The box is ticked or the description box says
  so, but the status comes from an endorsement to the policy. Ask for the
  endorsement. A tick is not an endorsement.
- **Waiver of subrogation.** Same: it lives in the policy.
- **Primary and non-contributory.** Same.
- **Whether the coverage responds to this project.** Exclusions live in the
  policy. A professional liability policy excluding a project type, a
  jurisdiction, or a delivery method will show none of that on a certificate.

Also check: the cancellation notice wording, which usually promises nothing; the
dates, against the project period rather than against today; the named insured,
against the entity actually in the contract, which is often a different one.

### Step 5 — Report

- What the certificate shows, line by line.
- Where it does not meet the contract, individually.
- The four things it does not establish, and what to request for each.
- Any mismatch in named insured, dates, or project description.
- What to ask the broker, as a list they can act on.

Close by saying this is not insurance advice and that the policy governs.

## Rules

- **Say what a certificate is, first, every run.**
- **Never state what a policy covers.** Only what the certificate shows.
- Compare against the contract's quoted requirement, never against a
  recollection of what is usual.
- Check per-occurrence and aggregate limits separately, and ask about
  per-project aggregate.
- Name the four things a certificate does not establish, every run.
- Check the named insured against the contracting entity.
- Never confirm that coverage is adequate.

## Anti-patterns

- Treating a ticked additional insured box as an endorsement.
- Filing a certificate as proof of compliance.
- Recalling what limits are customary.
- Reading the dates against today instead of against the project period.
- Ignoring that professional liability is claims-made.
- Missing that the named insured is an affiliate rather than the contracting
  entity.
- Advising on adequacy of coverage.
