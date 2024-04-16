<template>
  <div>
    <UserNavbar :id_="3"></UserNavbar>
    <h2>Create Category</h2>
    <form @submit.prevent="createCategory">
      <label for="categoryName">Category Name:</label>
      <input type="text" id="categoryName" v-model="categoryName" required>
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script>
import UserNavbar from "../components/UserNavbar.vue";

export default {
  name: "AdminCreateCategory",
  components: { UserNavbar, FAQForm, SearchTicket },
  data() {
    return {
      categoryName: '' // stores the value of the category name input field
    };
  },
  mounted() {},
  methods: {
    async createCategory() {
      try {
        const response = await fetch('/api/create-category', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ categoryName: this.categoryName })
        });

        if (!response.ok) {
          throw new Error('Failed to create category');
        }

        const responseData = await response.json();
        console.log('Category created successfully:', responseData);
        // Reset the input field after submitting
        this.categoryName = '';
      } catch (error) {
        console.error('Error creating category:', error.message);
      }
    }
  },
  computed: {},
};
</script>

<style></style>
