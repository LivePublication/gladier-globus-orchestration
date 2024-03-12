# Gladier / Globus Interface for CLI Development 🛠️

This repository provides a simple Gladier/Globus script for generating Workflow Execution Plans (WEPs) for testing and integrating the LivePublication CLI/SDK. The current focus of CLI/SDK development is on embedding prospective entities within the [Provenance Run Crate](https://www.researchobject.org/workflow-run-crate/profiles/provenance_run_crate) during the initialization of a Gladier-Globus flow.

A discussion on the alignment of Provenance crates, the Gladier-Globus context, and LivePublication can be found [here](https://www.overleaf.com/read/yhmhgvkhstyh#08d871).

### Transfers as aliases

Gladier has been updated to provide alias functionality for transfer steps in a gladier-globus flow. This removes the issue of having to write seperate gladier components for each transfer step, meaning we can cut down on redundant work. Find an example [here](https://github.com/globus-gladier/gladier-client-examples/blob/main/tar-and-transfer/client.py).
