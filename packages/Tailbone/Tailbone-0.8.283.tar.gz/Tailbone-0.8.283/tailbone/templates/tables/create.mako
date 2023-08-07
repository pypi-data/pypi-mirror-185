## -*- coding: utf-8; -*-
<%inherit file="/master/create.mako" />

<%def name="extra_styles()">
  ${parent.extra_styles()}
  <style type="text/css">
    .label {
        white-space: nowrap;
    }
  </style>
</%def>

<%def name="render_this_page()">
  <b-steps v-model="activeStep"
           :animated="false"
           rounded
           :has-navigation="false"
           vertical
           icon-pack="fas">

    <b-step-item step="1"
                 value="enter-details"
                 label="Enter Details"
                 clickable>
      <h3 class="is-size-3 block">
        Enter Details
      </h3>

      <b-field label="Schema Branch" horizontal
               message="Leave this set to your custom app branch, unless you know what you're doing.">
        <b-select v-model="tableBranch">
          <option v-for="branch in branchOptions"
                  :key="branch"
                  :value="branch">
            {{ branch }}
          </option>
        </b-select>
      </b-field>

      <b-field grouped>

        <b-field label="Table Name"
                 message="Should be singular in nature, i.e. 'widget' not 'widgets'">
          <b-input v-model="tableName">
          </b-input>
        </b-field>

        <b-field label="Model/Class Name"
                 message="Should be singular in nature, i.e. 'Widget' not 'Widgets'">
          <b-input v-model="tableModelName">
          </b-input>
        </b-field>

      </b-field>

      <b-field grouped>

        <b-field label="Model Title"
                 message="Human-friendly singular model title.">
          <b-input v-model="tableModelTitle">
          </b-input>
        </b-field>

        <b-field label="Model Title Plural"
                 message="Human-friendly plural model title.">
          <b-input v-model="tableModelTitlePlural">
          </b-input>
        </b-field>

      </b-field>

      <b-field label="Description"
               message="Brief description of what a record in this table represents.">
        <b-input v-model="tableDescription">
        </b-input>
      </b-field>

      <b-field>
        <b-checkbox v-model="tableVersioned">
          Record version data for this table
        </b-checkbox>
      </b-field>

      <br />

      <div class="level-left">
        <div class="level-item">
          <h4 class="block is-size-4">Columns</h4>
        </div>
        <div class="level-item">
          <b-button type="is-primary"
                    icon-pack="fas"
                    icon-left="plus"
                    @click="tableAddColumn()">
            New
          </b-button>
        </div>
      </div>

      <b-table
        :data="tableColumns">
        % if buefy_0_8:
        <template slot-scope="props">
          % endif

          <b-table-column field="name"
                          label="Name"
                          % if not buefy_0_8:
                          v-slot="props"
                          % endif
                          >
            {{ props.row.name }}
          </b-table-column>

          <b-table-column field="data_type"
                          label="Data Type"
                          % if not buefy_0_8:
                          v-slot="props"
                          % endif
                          >
            {{ props.row.data_type }}
          </b-table-column>

          <b-table-column field="nullable"
                          label="Nullable"
                          % if not buefy_0_8:
                          v-slot="props"
                          % endif
                          >
            {{ props.row.nullable ? "Yes" : "No" }}
          </b-table-column>

          <b-table-column field="versioned"
                          label="Versioned"
                          :visible="tableVersioned"
                          % if not buefy_0_8:
                          v-slot="props"
                          % endif
                          >
            {{ props.row.versioned ? "Yes" : "No" }}
          </b-table-column>

          <b-table-column field="description"
                          label="Description"
                          % if not buefy_0_8:
                          v-slot="props"
                          % endif
                          >
            {{ props.row.description }}
          </b-table-column>

          <b-table-column field="actions"
                          label="Actions"
                          % if not buefy_0_8:
                          v-slot="props"
                          % endif
                          >
            <a v-if="props.row.name != 'uuid'"
               href="#"
               @click.prevent="tableEditColumn(props.row)">
              <i class="fas fa-edit"></i>
              Edit
            </a>
            &nbsp;

            <a v-if="props.row.name != 'uuid'"
               href="#"
               class="has-text-danger"
               @click.prevent="tableDeleteColumn(props.index)">
              <i class="fas fa-trash"></i>
              Delete
            </a>
            &nbsp;
          </b-table-column>

          % if buefy_0_8:
        </template>
        % endif
      </b-table>

      <b-modal has-modal-card
               :active.sync="editingColumnShowDialog">
        <div class="modal-card">

          <header class="modal-card-head">
            <p class="modal-card-title">
              {{ (editingColumn && editingColumn.name) ? "Edit" : "New" }} Column
            </p>
          </header>

          <section class="modal-card-body">

            <b-field label="Name">
              <b-input v-model="editingColumnName"
                       ref="editingColumnName">
              </b-input>
            </b-field>

            <b-field label="Data Type">
              <b-input v-model="editingColumnDataType"></b-input>
            </b-field>

            <b-field grouped>

            <b-field label="Nullable">
              <b-checkbox v-model="editingColumnNullable"
                          native-value="true">
                {{ editingColumnNullable }}
              </b-checkbox>
            </b-field>

            <b-field label="Versioned"
                     v-if="tableVersioned">
              <b-checkbox v-model="editingColumnVersioned"
                          native-value="true">
                {{ editingColumnVersioned }}
              </b-checkbox>
            </b-field>

            </b-field>

            <b-field label="Description">
              <b-input v-model="editingColumnDescription"></b-input>
            </b-field>

          </section>

          <footer class="modal-card-foot">
            <b-button @click="editingColumnShowDialog = false">
              Cancel
            </b-button>
            <b-button type="is-primary"
                      icon-pack="fas"
                      icon-left="save"
                      @click="editingColumnSave()">
              Save
            </b-button>
          </footer>
        </div>
      </b-modal>

      <br />

      <div class="buttons">
        <b-button type="is-primary"
                  icon-pack="fas"
                  icon-left="check"
                  @click="activeStep = 'write-model'">
          Details are complete
        </b-button>
      </div>

    </b-step-item>

    <b-step-item step="2"
                 value="write-model"
                 label="Write Model">
      <h3 class="is-size-3 block">
        Write Model
      </h3>

      <b-field label="Schema Branch" horizontal>
        {{ tableBranch }}
      </b-field>

      <b-field label="Table Name" horizontal>
        {{ tableName }}
      </b-field>

      <b-field label="Model Class" horizontal>
        {{ tableModelName }}
      </b-field>

      <b-field horizontal label="File">
        <b-input v-model="tableModelFile"></b-input>
      </b-field>

      <div class="form">
        <div class="buttons">
          <b-button icon-pack="fas"
                    icon-left="arrow-left"
                    @click="activeStep = 'enter-details'">
            Back
          </b-button>
          <b-button type="is-primary"
                    icon-pack="fas"
                    icon-left="save"
                    @click="writeModelFile()"
                    :disabled="writingModelFile">
            {{ writingModelFile ? "Working, please wait..." : "Write model class to file" }}
          </b-button>
        </div>
      </div>
    </b-step-item>

    <b-step-item step="3"
                 value="review-model"
                 label="Review Model">
      <h3 class="is-size-3 block">
        Review Model
      </h3>
      <p class="block">TODO: review model class here</p>
      <div class="buttons">
        <b-button icon-pack="fas"
                  icon-left="arrow-left"
                  @click="activeStep = 'write-model'">
          Back
        </b-button>
        <b-button type="is-primary"
                  icon-pack="fas"
                  icon-left="check"
                  @click="activeStep = 'write-revision'">
          Model class looks good!
        </b-button>
      </div>
    </b-step-item>

    <b-step-item step="4"
                 value="write-revision"
                 label="Write Revision">
      <h3 class="is-size-3 block">
        Write Revision
      </h3>
      <p class="block">
        You said the model class looked good, so next we will generate
        a revision script, used to modify DB schema.
      </p>
      <p class="block">
        TODO: write revision script here
      </p>
      <div class="buttons">
        <b-button icon-pack="fas"
                  icon-left="arrow-left"
                  @click="activeStep = 'review-model'">
          Back
        </b-button>
        <b-button type="is-primary"
                  icon-pack="fas"
                  icon-left="save"
                  @click="activeStep = 'review-revision'">
          Write revision script to file
        </b-button>
      </div>
    </b-step-item>

    <b-step-item step="5"
                 value="review-revision"
                 label="Review Revision">
      <h3 class="is-size-3 block">
        Review Revision
      </h3>
      <p class="block">TODO: review revision script here</p>
      <div class="buttons">
        <b-button icon-pack="fas"
                  icon-left="arrow-left"
                  @click="activeStep = 'write-revision'">
          Back
        </b-button>
        <b-button type="is-primary"
                  icon-pack="fas"
                  icon-left="check"
                  @click="activeStep = 'upgrade-db'">
          Revision script looks good!
        </b-button>
      </div>
    </b-step-item>

    <b-step-item step="6"
                 value="upgrade-db"
                 label="Upgrade DB">
      <h3 class="is-size-3 block">
        Upgrade DB
      </h3>
      <p class="block">TODO: upgrade DB here</p>
      <div class="buttons">
        <b-button icon-pack="fas"
                  icon-left="arrow-left"
                  @click="activeStep = 'review-revision'">
          Back
        </b-button>
        <b-button type="is-primary"
                  icon-pack="fas"
                  icon-left="check"
                  @click="activeStep = 'review-db'">
          Upgrade database
        </b-button>
      </div>
    </b-step-item>

    <b-step-item step="7"
                 value="review-db"
                 label="Review DB">
      <h3 class="is-size-3 block">
        Review DB
      </h3>
      <p class="block">TODO: review DB here</p>
      <div class="buttons">
        <b-button icon-pack="fas"
                  icon-left="arrow-left"
                  @click="activeStep = 'upgrade-db'">
          Back
        </b-button>
        <b-button type="is-primary"
                  icon-pack="fas"
                  icon-left="check"
                  @click="activeStep = 'commit-code'">
          DB looks good!
        </b-button>
      </div>
    </b-step-item>

    <b-step-item step="8"
                 value="commit-code"
                 label="Commit Code">
      <h3 class="is-size-3 block">
        Commit Code
      </h3>
      <p class="block">TODO: commit changes here</p>
      <div class="buttons">
        <b-button icon-pack="fas"
                  icon-left="arrow-left"
                  @click="activeStep = 'review-db'">
          Back
        </b-button>
        <b-button type="is-primary"
                  icon-pack="fas"
                  icon-left="check"
                  @click="alert('TODO: redirect to table view')">
          Code changes are committed!
        </b-button>
      </div>
    </b-step-item>
  </b-steps>
</%def>

<%def name="modify_this_page_vars()">
  ${parent.modify_this_page_vars()}
  <script type="text/javascript">

    ThisPageData.activeStep = null
    ThisPageData.branchOptions = ${json.dumps(branch_name_options)|n}

    ThisPageData.tableBranch = ${json.dumps(branch_name)|n}
    ThisPageData.tableName = '${rattail_app.get_table_prefix()}_widget'
    ThisPageData.tableModelName = '${rattail_app.get_class_prefix()}Widget'
    ThisPageData.tableModelTitle = 'Widget'
    ThisPageData.tableModelTitlePlural = 'Widgets'
    ThisPageData.tableDescription = "Represents a cool widget."
    ThisPageData.tableVersioned = true

    ThisPageData.tableColumns = [{
        name: 'uuid',
        data_type: 'String(length=32)',
        nullable: false,
        description: "UUID primary key",
        versioned: true,
    }]

    ThisPageData.editingColumnShowDialog = false
    ThisPageData.editingColumn = null
    ThisPageData.editingColumnName = null
    ThisPageData.editingColumnDataType = null
    ThisPageData.editingColumnNullable = true
    ThisPageData.editingColumnDescription = null
    ThisPageData.editingColumnVersioned = true

    ThisPage.methods.tableAddColumn = function() {
        this.editingColumn = null
        this.editingColumnName = null
        this.editingColumnDataType = null
        this.editingColumnNullable = true
        this.editingColumnDescription = null
        this.editingColumnVersioned = true
        this.editingColumnShowDialog = true
        this.$nextTick(() => {
            this.$refs.editingColumnName.focus()
        })
    }

    ThisPage.methods.tableEditColumn = function(column) {
        this.editingColumn = column
        this.editingColumnName = column.name
        this.editingColumnDataType = column.data_type
        this.editingColumnNullable = column.nullable
        this.editingColumnDescription = column.description
        this.editingColumnVersioned = column.versioned
        this.editingColumnShowDialog = true
        this.$nextTick(() => {
            this.$refs.editingColumnName.focus()
        })
    }

    ThisPage.methods.editingColumnSave = function() {
        let column
        if (this.editingColumn) {
            column = this.editingColumn
        } else {
            column = {}
            this.tableColumns.push(column)
        }

        column.name = this.editingColumnName
        column.data_type = this.editingColumnDataType
        column.nullable = this.editingColumnNullable
        column.description = this.editingColumnDescription
        column.versioned = this.editingColumnVersioned

        this.editingColumnShowDialog = false
    }

    ThisPage.methods.tableDeleteColumn = function(index) {
        if (confirm("Really delete this column?")) {
            this.tableColumns.splice(index, 1)
        }
    }

    ThisPageData.tableModelFile = '${model_dir}widget.py'
    ThisPageData.writingModelFile = false

    ThisPage.methods.writeModelFile = function() {
        this.writingModelFile = true

        let url = '${url('{}.write_model_file'.format(route_prefix))}'
        let params = {
            branch_name: this.tableBranch,
            table_name: this.tableName,
            model_name: this.tableModelName,
            model_title: this.tableModelTitle,
            model_title_plural: this.tableModelTitlePlural,
            description: this.tableDescription,
            versioned: this.tableVersioned,
            module_file: this.tableModelFile,
            columns: this.tableColumns,
        }
        this.submitForm(url, params, response => {
            this.writingModelFile = false
            this.activeStep = 'review-model'
        }, response => {
            this.writingModelFile = false
        })
    }

  </script>
</%def>


${parent.body()}
