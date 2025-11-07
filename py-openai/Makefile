# $NetBSD$

DISTNAME=	openai-2.7.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	net python
MASTER_SITES=	${MASTER_SITE_PYPI:=o/openai/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/openai/
COMMENT=	OpenAI API
LICENSE=	apache-2.0

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-httpx>=0:../../www/py-httpx
DEPENDS+=	${PYPKGPREFIX}-pydantic>=0:../../devel/py-pydantic
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-anyio>=0:../../devel/py-anyio
DEPENDS+=	${PYPKGPREFIX}-distro>=0:../../devel/py-distro
DEPENDS+=	${PYPKGPREFIX}-sniffio>=0:../../misc/py-sniffio
DEPENDS+=	${PYPKGPREFIX}-tqdm>=0:../../misc/py-tqdm
DEPENDS+=	${PYPKGPREFIX}-jiter>=0:../../pkgsrc_myownpkgs/py-jiter

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
