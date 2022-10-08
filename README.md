# Финальный проект Yamdb_final

![workflow](https://github.com/MakcAntov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

**Workflow** — это набор команд, которые выполнятся в виртуальном окружении после того, как произойдёт какое-то событие-триггер.

В этом проекте реализован *Workflow* для приложений **Continuous Integration** и **Continuous Deployment**:
* автоматический запуск тестов;
* обновление образов на Docker Hub;
* автоматический деплой на боевой сервер при `push` в главную ветку *main*.
* отправка уведомления в Telegram о том, что процесс деплоя успешно завершился.
