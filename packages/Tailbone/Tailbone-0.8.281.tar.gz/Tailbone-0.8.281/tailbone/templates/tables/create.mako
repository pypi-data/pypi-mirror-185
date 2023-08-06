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

<%def name="render_buefy_form()">
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
      ${parent.render_buefy_form()}
    </b-step-item>

    <b-step-item step="2"
                 value="write-model"
                 label="Write Model"
                 clickable>
      <h3 class="is-size-3 block">
        Write Model
      </h3>
      <div class="form">
        <b-field horizontal label="Table Name">
          <span>TODO: poser_widget</span>
        </b-field>
        <b-field horizontal label="Model Class">
          <span>TODO: PoserWidget</span>
        </b-field>
        <b-field horizontal label="File">
          <span>TODO: ~/src/poser/poser/db/model/widgets.py</span>
        </b-field>
        <div class="buttons">
          <b-button icon-pack="fas"
                    icon-left="arrow-left"
                    @click="activeStep = 'enter-details'">
            Back
          </b-button>
          <b-button type="is-primary"
                    icon-pack="fas"
                    icon-left="save"
                    @click="activeStep = 'review-model'">
            Write model class to file
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

  </script>
</%def>


${parent.body()}
