using Microsoft.EntityFrameworkCore;

namespace criticApi.Models
{
    public class CriticContext : DbContext
    {
        public CriticContext(DbContextOptions<CriticContext> options)
            : base(options)
        {
        }

        public DbSet<Record> Records { get; set; }
    }
}