### Directory structure

```
+- api - The API type
+- filters - Filters of the models
+- forms - The ModelForm, ModelFilterForm, ModelImportForm, ModelBulkEditForm
+- migrations - DB Django Migration
+- tables - The ModelBaseTable, ModelTable, RelatedModelTable
+- templates
  +- netbox_disk - The detail view of each model
    +- disk - The template content box in the Virtual Machine Model
+- views - PhysicalvolumeListView, PhysicalvolumeView, PhysicalvolumeEditView, PhysicalvolumeDeleteView, 
           PhysicalvolumeBulkImportView, PhysicalvolumeBulkEditView, PhysicalvolumeBulkDeleteView
```

Basis:
- pv:
  - size
  - Storage Cluster
  - virtual_machine

Windows Form:
- Laufwerk Name (D, E, F)
- filesystem (ntfs)

Linux Form:
- vg name
- lv name
- path
- filesystem


Extra Filesystem Model & als ChoiceField ausgeben

# Build
poetry publish --build



git add . && git commit -m "0.0.7.6.5.41" && git push