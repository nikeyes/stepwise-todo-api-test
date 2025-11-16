# Funcionalidades Candidatas para Stepwise-Dev

Este documento describe las mejores funcionalidades para implementar en el proyecto TODO API usando el plugin [stepwise-dev](https://github.com/nikeyes/stepwise-dev).

## ¿Qué es Stepwise-Dev?

Stepwise-dev es un plugin para Claude Code que implementa un flujo de trabajo estructurado en cuatro fases:

1. **Research** - Explorar y documentar la base de código
2. **Plan** - Crear planes de implementación detallados e iterativos
3. **Implement** - Ejecutar fase por fase con validaciones
4. **Validate** - Verificar sistemáticamente la implementación completa

**Problema que resuelve:** Los LLMs pierden atención después del 60% de uso del contexto. Stepwise-dev mantiene coherencia limpiando contexto entre fases y persistiendo decisiones en `thoughts/`.

## Funcionalidades Ideales para Stepwise-Dev

### 1. Sistema de Autenticación/Autorización ⭐⭐⭐⭐⭐

**Por qué es perfecta para stepwise:**
- Requiere investigación de librerías (JWT, OAuth2, FastAPI Security)
- Necesita planificación arquitectónica (middleware, dependencias, modelos de usuario)
- Implementación en múltiples capas (auth endpoints, protección de rutas, storage de usuarios)
- Validación compleja (tokens, permisos, tests de seguridad)

**Pasos naturales:**
- **Research**: Explorar patrones de auth en FastAPI, decidir estrategia (JWT vs sesiones)
- **Plan**: Diseñar flujo de login/register, estructura de usuarios, middlewares
- **Implement**: Crear modelos, endpoints, proteger rutas existentes
- **Validate**: Tests de seguridad, verificar tokens, casos edge

### 2. Persistencia de Datos (SQLite/PostgreSQL) ⭐⭐⭐⭐⭐

**Por qué es perfecta:**
- Investigación de ORMs (SQLAlchemy, Tortoise-ORM)
- Planificación de migraciones y esquemas
- Refactorización del storage actual (`src/todo_api/storage.py`)
- Validación con tests de persistencia, transacciones

**Complejidad ideal:**
- Cambio arquitectónico significativo
- Requiere mantener compatibilidad con API existente
- Necesita documentar decisiones (¿por qué SQLite vs Postgres?)

**Consideraciones:**
- Migración de datos in-memory a persistente
- Sistema de migraciones (Alembic)
- Connection pooling y gestión de sesiones
- Tests de integridad referencial

### 3. Rate Limiting Middleware ⭐⭐⭐⭐

**Por qué funciona bien:**
- **Research**: Comparar slowapi, limits, Redis-based solutions
- **Plan**: Diseñar estrategias (por IP, por usuario autenticado, límites por endpoint)
- **Implement**: Middleware customizado con configuración
- **Validate**: Tests de carga, verificar headers X-RateLimit-*

**Aspectos a investigar:**
- Estrategias de almacenamiento (memoria, Redis)
- Configuración flexible por endpoint
- Headers estándar (X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset)
- Excepciones y whitelisting

### 4. Sistema de Búsqueda Avanzada ⭐⭐⭐⭐

**Más que el simple GET /todos/search:**
- **Research**: Full-text search, filtros combinados, paginación
- **Plan**: Query parameters (q, status, date_range, tags), ordenamiento
- **Implement**: Filtros complejos, índices, performance optimization
- **Validate**: Tests de casos edge, búsquedas complejas

**Features potenciales:**
- Búsqueda en título y descripción (case-insensitive)
- Filtros por estado (completed/pending)
- Filtros por fecha (created_at, updated_at)
- Ordenamiento multi-campo
- Paginación (limit, offset)
- Destacado de resultados (snippets)

### 5. Sistema de Tags/Categorías ⭐⭐⭐⭐

**Por qué es interesante:**
- **Research**: Decidir relación many-to-many vs simple array
- **Plan**: Nuevos modelos, endpoints para tags, asignación
- **Implement**: CRUD de tags, asociación con todos, búsqueda por tags
- **Validate**: Tests de relaciones, queries complejas

**Decisiones arquitectónicas:**
- Modelo de datos (tags como entidad separada vs campo en todo)
- Endpoints para gestión de tags
- Asignación múltiple de tags
- Auto-completado y sugerencias
- Conteo de uso por tag

## Funcionalidades Menos Apropiadas

### ❌ Endpoints Simples (PATCH, DELETE básicos)
- Demasiado sencillo para stepwise-dev
- No requiere research ni planificación profunda
- Mejor implementarlos directamente sin el overhead del plugin

### ❌ Formateo de Código o Linting
- Tareas mecánicas sin decisiones arquitectónicas
- No se benefician del flujo de múltiples fases

### ❌ Actualizaciones de Dependencias
- Proceso automatizable
- No requiere investigación contextual profunda

## Roadmap Sugerido

Para maximizar el valor de stepwise-dev, implementar **en este orden**:

### Fase 1: Autenticación 🔐
**Prioridad: Alta**
- Feature más compleja
- Base para funcionalidades futuras (ownership de todos, permisos)
- Múltiples decisiones arquitectónicas importantes

### Fase 2: Persistencia de Datos 💾
**Prioridad: Alta**
- Cambio arquitectónico fundamental
- Requiere migración de código existente
- Afecta a todas las demás features

### Fase 3: Rate Limiting ⏱️
**Prioridad: Media**
- Feature middleware independiente
- Buena práctica de producción
- No afecta a otras features

### Fase 4: Búsqueda Avanzada + Tags 🔍
**Prioridad: Media-Baja**
- Features combinadas que se complementan
- Mejoran significativamente la UX de la API
- Pueden implementarse juntas para máximo valor

## Beneficios del Enfoque Stepwise

Cada una de estas funcionalidades se beneficia del ciclo Research → Plan → Implement → Validate:

1. **Persistencia de decisiones**: El directorio `thoughts/` mantiene el razonamiento detrás de elecciones arquitectónicas
2. **Gestión de contexto**: Limpiar contexto entre fases evita degradación de atención del modelo
3. **Validación sistemática**: Cada fase tiene criterios claros de éxito
4. **Documentación implícita**: El proceso genera documentación natural del proyecto

## Cómo Usar Este Documento

1. Selecciona una funcionalidad del roadmap
2. Inicia stepwise-dev con el comando apropiado
3. Sigue el ciclo completo Research → Plan → Implement → Validate
4. Documenta aprendizajes y decisiones en `thoughts/`
5. Repite con la siguiente funcionalidad

## Referencias

- [Stepwise-Dev Plugin](https://github.com/nikeyes/stepwise-dev)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
